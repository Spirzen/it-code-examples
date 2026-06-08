
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;

import java.io.IOException;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@RestController
public class SseEmitterController {
    
    private final Map<String, SseEmitter> emitters = new ConcurrentHashMap<>();
    private final ExecutorService executor = Executors.newCachedThreadPool();
    
    @GetMapping(value = "/sse", produces = "text/event-stream")
    public SseEmitter handleSse() {
        SseEmitter emitter = new SseEmitter(Long.MAX_VALUE); // Без таймаута
        
        String emitterId = "emitter-" + System.currentTimeMillis();
        emitters.put(emitterId, emitter);
        
        // Настройка обработчиков
        emitter.onCompletion(() -> {
            System.out.println("SSE завершён: " + emitterId);
            emitters.remove(emitterId);
        });
        
        emitter.onTimeout(() -> {
            System.out.println("SSE таймаут: " + emitterId);
            emitters.remove(emitterId);
        });
        
        emitter.onError(error -> {
            System.out.println("SSE ошибка: " + emitterId + " - " + error.getMessage());
            emitters.remove(emitterId);
        });
        
        // Отправка начального сообщения
        try {
            emitter.send(SseEmitter.event()
                .name("connected")
                .data("{\"status\":\"connected\",\"id\":\"" + emitterId + "\"}"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        // Запуск потока отправки событий
        executor.submit(() -> {
            int count = 0;
            try {
                while (true) {
                    Thread.sleep(2000);
                    
                    if (!emitters.containsKey(emitterId)) {
                        break;
                    }
                    
                    count++;
                    emitter.send(SseEmitter.event()
                        .id(String.valueOf(count))
                        .name("tick")
                        .data("{\"count\":" + count + ",\"time\":" + System.currentTimeMillis() + "}"));
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            } catch (IOException e) {
                System.out.println("Ошибка отправки: " + e.getMessage());
                emitters.remove(emitterId);
            }
        });
        
        return emitter;
    }
    
    /**
     * Broadcast сообщения всем подключенным клиентам
     */
    public void broadcast(String eventName, Object data) {
        emitters.forEach((id, emitter) -> {
            try {
                emitter.send(SseEmitter.event()
                    .name(eventName)
                    .data(data));
            } catch (IOException e) {
                System.out.println("Ошибка broadcast для " + id + ": " + e.getMessage());
                emitters.remove(id);
            }
        });
    }
}
