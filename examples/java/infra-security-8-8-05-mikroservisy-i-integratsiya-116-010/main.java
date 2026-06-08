
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.http.MediaType;
import org.springframework.http.codec.ServerSentEvent;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Sinks;
import reactor.util.concurrent.Queues;

import java.time.Duration;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;

@RestController
public class SseController {
    
    // Хранилище для клиентских потоков
    private final Map<String, Sinks.Many<String>> clientSinks = new ConcurrentHashMap<>();
    private final AtomicInteger clientIdGenerator = new AtomicInteger(0);
    
    /**
     * Простой поток событий с фиксированным интервалом
     */
    @GetMapping(value = "/events", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> getEvents() {
        return Flux.interval(Duration.ofSeconds(2))
            .map(sequence -> ServerSentEvent.<String>builder()
                .id(String.valueOf(sequence))
                .event("tick")
                .data(String.format("{\"sequence\":%d,\"timestamp\":%d}",
                    sequence, System.currentTimeMillis()))
                .build());
    }
    
    /**
     * Поток с автоматическим переподключением
     */
    @GetMapping(value = "/stream", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> eventStream() {
        return Flux.interval(Duration.ofSeconds(1))
            .take(30) // Ограничение для демонстрации
            .map(sequence -> {
                if (sequence == 0) {
                    // Первое событие с указанием интервала повтора
                    return ServerSentEvent.<String>builder()
                        .event("connected")
                        .data("{\"status\":\"connected\"}")
                        .build();
                } else if (sequence == 1) {
                    // Установка интервала повтора
                    return ServerSentEvent.<String>builder()
                        .comment("retry: 5000")
                        .build();
                } else {
                    return ServerSentEvent.<String>builder()
                        .id(String.valueOf(sequence))
                        .event("message")
                        .data(String.format("{\"count\":%d,\"time\":%d}",
                            sequence, System.currentTimeMillis()))
                        .build();
                }
            });
    }
    
    /**
     * Broadcast уведомлений для всех подключенных клиентов
     */
    @GetMapping(value = "/notifications", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> notificationsStream() {
        String clientId = "client-" + clientIdGenerator.incrementAndGet();
        Sinks.Many<String> sink = Sinks.many().unicast().onBackpressureBuffer(Queues.SMALL_BUFFER_SIZE);
        
        clientSinks.put(clientId, sink);
        
        System.out.println("Новый клиент подключился: " + clientId);
        
        // Отправка приветственного сообщения
        sink.tryEmitNext("{\"type\":\"connected\",\"clientId\":\"" + clientId + "\"}");
        
        return sink.asFlux()
            .map(payload -> ServerSentEvent.<String>builder()
                .data(payload)
                .build())
            .doFinally(signalType -> {
                System.out.println("Клиент отключился: " + clientId);
                clientSinks.remove(clientId);
            });
    }
    
    /**
     * Отправка уведомления всем клиентам
     */
    public void broadcastNotification(String type, String title, String body) {
        String message = String.format(
            "{\"type\":\"%s\",\"title\":\"%s\",\"body\":\"%s\",\"timestamp\":%d}",
            type, title, body, System.currentTimeMillis()
        );
        
        clientSinks.forEach((clientId, sink) -> {
            sink.tryEmitNext(message);
        });
    }
    
    /**
     * Пример использования broadcast
     */
    public void simulateNotifications() {
        new Thread(() -> {
            int count = 0;
            while (true) {
                try {
                    Thread.sleep(3000);
                    count++;
                    broadcastNotification(
                        "info",
                        "Уведомление #" + count,
                        "Тестовое уведомление в " + System.currentTimeMillis()
                    );
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
        }).start();
    }
}
