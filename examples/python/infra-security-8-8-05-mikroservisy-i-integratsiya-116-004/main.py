from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import Dict, Set

import json
import asyncio

app = FastAPI()

# Хранилище подключений
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.rooms: Dict[str, Set[str]] = {}
    
    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        self.active_connections[client_id] = websocket
        print(f"Новое соединение: {client_id}")
    
    def disconnect(self, client_id: str):
        if client_id in self.active_connections:
            del self.active_connections[client_id]
            print(f"Соединение закрыто: {client_id}")
        
        # Удалить из всех комнат
        for room in self.rooms.values():
            room.discard(client_id)
    
    async def send_personal_message(self, message: dict, client_id: str):
        if client_id in self.active_connections:
            websocket = self.active_connections[client_id]
            await websocket.send_text(json.dumps(message))
    
    async def broadcast(self, message: dict, room: str = None):
        if room and room in self.rooms:
            recipients = self.rooms[room]
        else:
            recipients = self.active_connections.keys()
        
        data = json.dumps(message)
        disconnected = []
        
        for client_id in recipients:
            if client_id in self.active_connections:
                websocket = self.active_connections[client_id]
                try:
                    await websocket.send_text(data)
                except Exception:
                    disconnected.append(client_id)
        
        # Очистить мёртвые соединения
        for client_id in disconnected:
            self.disconnect(client_id)

manager = ConnectionManager()

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket, client_id)
    
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            
            msg_type = message.get("type")
            
            if msg_type == "ping":
                await manager.send_personal_message({
                    "type": "pong",
                    "timestamp": asyncio.get_event_loop().time()
                }, client_id)
            
            elif msg_type == "join":
                room = message.get("room")
                if room:
                    if room not in manager.rooms:
                        manager.rooms[room] = set()
                    manager.rooms[room].add(client_id)
                    
                    await manager.broadcast({
                        "type": "user_joined",
                        "client_id": client_id,
                        "room": room
                    }, room)
            
            elif msg_type == "message":
                room = message.get("room")
                await manager.broadcast({
                    "type": "message",
                    "client_id": client_id,
                    "text": message.get("text"),
                    "timestamp": asyncio.get_event_loop().time()
                }, room)
    
    except WebSocketDisconnect:
        manager.disconnect(client_id)
    except Exception as e:
        print(f"Ошибка: {e}")
        manager.disconnect(client_id)

@app.get("/")
async def get():
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>WebSocket Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <div id="messages"></div>
        <input id="message" type="text" />
        <button onclick="sendMessage()">Send</button>
        
        <script>
            const ws = new WebSocket("ws://localhost:8000/ws/test_client");
            
            ws.onmessage = (event) => {
                const messages = document.getElementById('messages');
                const data = JSON.parse(event.data);
                const message = document.createElement('div');
                message.textContent = JSON.stringify(data);
                messages.appendChild(message);
            };
            
            function sendMessage() {
                const input = document.getElementById('message');
                ws.send(JSON.stringify({
                    type: 'message',
                    text: input.value
                }));
                input.value = '';
            }
        </script>
    </body>
    </html>
    """)
