# Python — создание очереди через HTTP API

import requests

requests.put(
    "http://admin:pass@localhost:15672/api/queues/%2F/orders",
    json={
        "durable": True,
        "arguments": {
            "x-queue-type": "quorum",
            "x-dead-letter-exchange": "dlx.orders"
        }
    }
)
