// HTTP-запросы к ksqlDB REST API
const fetch = require('node-fetch');

async function createStream() {
    const query = `
        CREATE STREAM orders_stream (
            type VARCHAR,
            orderId VARCHAR,
            customerId VARCHAR,
            items ARRAY<STRUCT<productId VARCHAR, quantity INT, price DOUBLE>>,
            timestamp VARCHAR
        ) WITH (
            kafka_topic='orders',
            value_format='json',
            partitions=4
        );
`;
    
    await fetch('http://localhost:8088/ksql', {
        method: 'POST',
        headers: { 'Content-Type': 'application/vnd.ksql.v1+json' },
        body: JSON.stringify({ ksql: query })
    });
}

async function createAggregation() {
    const query = `
        CREATE TABLE customer_order_count AS
        SELECT customerId, COUNT(*) AS orderCount
        FROM orders_stream
        GROUP BY customerId
        EMIT CHANGES;
`;
    
    await fetch('http://localhost:8088/ksql', {
        method: 'POST',
        headers: { 'Content-Type': 'application/vnd.ksql.v1+json' },
        body: JSON.stringify({ ksql: query })
    });
}

async function queryOrders() {
    const response = await fetch('http://localhost:8088/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/vnd.ksql.v1+json' },
        body: JSON.stringify({
            ksql: "SELECT * FROM customer_order_count WHERE customerId = 'customer-456';"
        })
    });
    
    const data = await response.json();
    console.log('Результаты:', data);
}
