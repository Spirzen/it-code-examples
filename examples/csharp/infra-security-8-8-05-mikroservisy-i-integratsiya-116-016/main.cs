// Пример агрегации с использованием Kafka Streams API (Java-библиотека через IKVM или REST Proxy)
// Для .NET можно использовать Kafka REST Proxy или Confluent Cloud ksqlDB

public class OrderAnalytics
{
    // Подсчёт заказов по клиентам
    /*
    CREATE TABLE customer_order_count AS
    SELECT customer_id, COUNT(*) AS order_count
    FROM orders
    GROUP BY customer_id
    EMIT CHANGES;
    */

    // Средний чек по периодам
    /*
    CREATE TABLE avg_order_value AS
    SELECT 
        WINDOWSTART() as period_start,
        COUNT(*) as order_count,
        AVG(total_amount) as avg_amount
    FROM orders
    WINDOW TUMBLING (SIZE 1 HOUR)
    GROUP BY WINDOWSTART()
    EMIT CHANGES;
    */
}
