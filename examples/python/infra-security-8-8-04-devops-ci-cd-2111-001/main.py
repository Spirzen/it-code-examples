from prometheus_client import Counter, Histogram

REQUESTS = Counter("http_requests_total", "Запросы", ["method", "route", "status"])
LATENCY = Histogram("http_request_duration_seconds", "Latency", ["route"])

@app.middleware("http")
async def metrics_middleware(request, call_next):
    with LATENCY.labels(route=request.url.path).time():
        response = await call_next(request)
    REQUESTS.labels(
        method=request.method,
        route=request.url.path,
        status=response.status_code,
    ).inc()
    return response
