class ApplicationState:
    def __init__(self):
        self.started_at = datetime.utcnow()
        self.ready = False
        self.components_ready = {
            "database": False,
            "cache": False,
            "references": False
        }
    
    async def wait_for_readiness(self, timeout: float = 30.0):
        """Ожидание готовности всех компонентов."""
        start = time.monotonic()
        while time.monotonic() - start < timeout:
            if all(self.components_ready.values()):
                self.ready = True
                return True
            await asyncio.sleep(0.1)
        return False

@app.middleware("http")
async def readiness_middleware(request: Request, call_next):
    """Отказ в обслуживании до полной готовности."""
    if not app.state.ready:
        # Возврат 503 до готовности
        return JSONResponse(
            status_code=503,
            content={
                "error": "service_starting",
                "message": "Приложение завершает инициализацию",
                "components": app.state.components_ready
            }
        )
    return await call_next(request)
