# Опасный паттерн — полное логирование в горячем пути
@app.middleware("http")
async def verbose_logging_middleware(request: Request, call_next):
    request_body = await request.body()
    logger.info(
        "Входящий запрос",
        method=request.method,
        path=request.url.path,
        headers=dict(request.headers),
        body=request_body.decode("utf-8"),
        client_ip=request.client.host
    )
    
    response = await call_next(request)
    
    logger.info(
        "Исходящий ответ",
        status_code=response.status_code,
        headers=dict(response.headers)
    )
    return response
