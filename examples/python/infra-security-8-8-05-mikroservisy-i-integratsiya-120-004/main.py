from fastapi import FastAPI, Header, HTTPException

import hmac
import hashlib

app = FastAPI()

@app.post("/webhook/orders")
async def handle_webhook(
    payload: dict,
    x_signature: str = Header(None)
):
    # Проверка подлинности через HMAC
    expected = hmac.new(
        key=WEBHOOK_SECRET.encode(),
        msg=await request.body(),
        digestmod=hashlib.sha256
    ).hexdigest()
    
    if not hmac.compare_digest(f"x-sha256={expected}", x_signature or ""):
        raise HTTPException(status_code=401, detail="Invalid signature")
    
    # Идемпотентная обработка
    event_id = payload.get("event_id")
    if event_id and is_event_processed(event_id):
        return {"status": "duplicate"}
    
    process_event(payload)
    mark_event_processed(event_id)
    
    return {"status": "accepted"}  # 200 OK немедленно для подтверждения доставки
