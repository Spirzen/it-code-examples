
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.*;
import org.apache.kafka.streams.kstream.*;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

import java.time.Duration;
import java.util.Properties;

@Component
public class OrderAnalyticsStreams {
    
    @Bean
    public KafkaStreams orderAnalyticsStreams() {
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "order-analytics-app");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        
        StreamsBuilder builder = new StreamsBuilder();
        
        // Чтение событий заказов
        KStream<String, String> orders = builder.stream("orders");
        
        // Фильтрация только созданных заказов
        KStream<String, OrderEvent> createdOrders = orders
            .filter((key, value) -> value.contains("\"type\":\"OrderCreated\""))
            .mapValues(value -> parseOrderEvent(value));
        
        // Агрегация по клиентам
        KTable<String, Long> customerOrderCount = createdOrders
            .groupBy((key, event) -> event.customerId)
            .count(Materialized.as("customer-order-count"));
        
        // Подсчёт среднего чека по часам
        KTable<Windowed<String>, Double> hourlyAvgOrderValue = createdOrders
            .filter((key, event) -> event.totalAmount > 0)
            .groupBy((key, event) -> "all")
            .windowedBy(TimeWindows.of(Duration.ofHours(1)))
            .aggregate(
                () -> 0.0,
                (key, event, total) -> total + event.totalAmount,
                (key, event, total) -> total - event.totalAmount,
                Materialized.as("hourly-total-amount")
            )
            .mapValues(total -> total / 100.0); // Пример вычисления
        
        // Вывод результатов в топики
        customerOrderCount
            .toStream()
            .to("customer-order-count", Produced.with(Serdes.String(), Serdes.Long()));
        
        KafkaStreams streams = new KafkaStreams(builder.build(), props);
        streams.start();
        
        Runtime.getRuntime().addShutdownHook(new Thread(streams::close));
        
        return streams;
    }
    
    private OrderEvent parseOrderEvent(String json) {
        // Парсинг JSON в объект OrderEvent
        return new OrderEvent();
    }
    
    private static class OrderEvent {
        String customerId;
        double totalAmount;
    }
}
