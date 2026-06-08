from fastapi import FastAPI, Response, Request, HTTPException
from fastapi.responses import StreamingResponse
from typing import Dict, Any

import asyncio
import json
import time
import uvicorn

app = FastAPI()

def generate_sse_event(
    event_type: str = "message",
    data: Any = None,
    event_id: str = None,
    retry: int = None
) -> str:
    """Форматирование события в формате SSE"""
    lines = []
    
    if event_id is not None:
        lines.append(f"id: {event_id}")
    
    if event_type != "message":
        lines.append(f"event: {event_type}")
    
    if data is not None:
        if isinstance(data, dict):
            data_str = json.dumps(data)
        else:
            data_str = str(data)
        
        # Многострочные данные
        for line in data_str.split('\n'):
            lines.append(f"data: {line}")
    
    if retry is not None:
        lines.append(f"retry: {retry}")
    
    lines.append("")  # Пустая строка завершает событие
    lines.append("")  # Двойной перевод строки
    
    return "\n".join(lines)

async def event_stream(request: Request, start_id: int = 0):
    """Генератор событий для SSE"""
    event_id = start_id
    
    # Отправка начального события
    yield generate_sse_event(
        event_type="connected",
        data={"message": "Подключено к потоку событий", "start_id": start_id},
        event_id=str(event_id)
    )
    event_id += 1
    
    # Установка интервала повтора
    yield generate_sse_event(retry=5000)
    
    try:
        while True:
            # Проверка отключения клиента
            if await request.is_disconnected():
                print("Клиент отключился")
                break
            
            # Генерация события
            event_data = {
                "id": event_id,
                "timestamp": time.time(),
                "message": f"Событие #{event_id}"
            }
            
            yield generate_sse_event(
                event_type="tick",
                data=event_data,
                event_id=str(event_id)
            )
            
            event_id += 1
            
            # Отправка комментария
            yield f": Серверное время {time.strftime('%H:%M:%S')}\n\n"
            
            await asyncio.sleep(2)
            
    except asyncio.CancelledError:
        print("Поток отменён")
        raise
    except Exception as e:
        print(f"Ошибка в потоке: {e}")
        yield generate_sse_event(
            event_type="error",
            data={"message": str(e)}
        )
    finally:
        # Финальное событие
        yield generate_sse_event(
            event_type="disconnected",
            data={"message": "Поток завершён"}
        )

@app.get("/events")
async def sse_endpoint(request: Request):
    """Эндпоинт для SSE потока"""
    
    # Получение последнего ID события
    last_event_id = request.headers.get("Last-Event-ID")
    start_id = int(last_event_id) if last_event_id else 0
    
    print(f"Подключение клиента, восстановление с события #{start_id}")
    
    return StreamingResponse(
        event_stream(request, start_id),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"  # Отключение буферизации nginx
        }
    )

# Симуляция уведомлений
notifications_store: Dict[int, Dict] = {}
notification_counter = 0

async def notification_stream(request: Request):
    """Поток уведомлений"""
    global notification_counter
    
    last_id = 0
    
    # Получение последнего события
    last_event_id = request.headers.get("Last-Event-ID")
    if last_event_id:
        last_id = int(last_event_id)
        print(f"Восстановление уведомлений с #{last_id}")
    
    try:
        while True:
            if await request.is_disconnected():
                break
            
            # Проверка новых уведомлений
            new_notifications = [
                (nid, payload) for nid, payload in notifications_store.items()
                if nid > last_id
            ]
            
            for nid, payload in sorted(new_notifications):
                yield generate_sse_event(
                    event_type="notification",
                    data=payload,
                    event_id=str(nid)
                )
                last_id = nid
            
            await asyncio.sleep(1)
            
    except asyncio.CancelledError:
        raise

@app.get("/notifications")
async def notifications_endpoint(request: Request):
    """Эндпоинт для потока уведомлений"""
    return StreamingResponse(
        notification_stream(request),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive"
        }
    )

@app.post("/notify")
async def create_notification(notification: Dict[str, Any]):
    """Создание нового уведомления"""
    global notification_counter
    
    notification_counter += 1
    
    notification_data = {
        "id": notification_counter,
        "type": notification.get("type", "info"),
        "title": notification.get("title", "Уведомление"),
        "body": notification.get("body", ""),
        "timestamp": time.time()
    }
    
    notifications_store[notification_counter] = notification_data
    
    return {"status": "created", "id": notification_counter}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
