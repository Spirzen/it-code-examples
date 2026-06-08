
import org.springframework.stereotype.Component;
import org.springframework.web.socket.CloseStatus;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import org.springframework.web.socket.handler.TextWebSocketHandler;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

@Component
public class WebSocketHandler extends TextWebSocketHandler {
    
    private final Map<String, WebSocketSession> sessions = new ConcurrentHashMap<>();
    
    @Override
    public void afterConnectionEstablished(WebSocketSession session) {
        String sessionId = session.getId();
        sessions.put(sessionId, session);
        
        System.out.println("Новое соединение: " + sessionId);
        
        try {
            session.sendMessage(new TextMessage(
                "{\"type\":\"welcome\",\"sessionId\":\"" + sessionId + "\"}"
            ));
        } catch (Exception e) {
            System.err.println("Ошибка отправки приветствия: " + e.getMessage());
        }
    }
    
    @Override
    protected void handleTextMessage(WebSocketSession session, TextMessage message) {
        String sessionId = session.getId();
        
        try {
            String payload = message.getPayload();
            System.out.println("Сообщение от " + sessionId + ": " + payload);
            
            // Эхо-ответ
            session.sendMessage(new TextMessage(
                "{\"type\":\"echo\",\"original\":" + payload + "}"
            ));
            
        } catch (Exception e) {
            System.err.println("Ошибка обработки сообщения: " + e.getMessage());
        }
    }
    
    @Override
    public void afterConnectionClosed(WebSocketSession session, CloseStatus status) {
        String sessionId = session.getId();
        sessions.remove(sessionId);
        
        System.out.println("Соединение закрыто: " + sessionId + " (" + status + ")");
    }
    
    @Override
    public void handleTransportError(WebSocketSession session, Throwable exception) {
        System.err.println("Ошибка транспорта: " + exception.getMessage());
    }
    
    // Метод для отправки сообщения конкретному клиенту
    public void sendMessageTo(String sessionId, String message) {
        WebSocketSession session = sessions.get(sessionId);
        if (session != null && session.isOpen()) {
            try {
                session.sendMessage(new TextMessage(message));
            } catch (Exception e) {
                System.err.println("Ошибка отправки: " + e.getMessage());
            }
        }
    }
    
    // Метод для рассылки всем клиентам
    public void broadcast(String message) {
        TextMessage textMessage = new TextMessage(message);
        
        sessions.forEach((sessionId, session) -> {
            if (session.isOpen()) {
                try {
                    session.sendMessage(textMessage);
                } catch (Exception e) {
                    System.err.println("Ошибка рассылки: " + e.getMessage());
                }
            }
        });
    }
}
