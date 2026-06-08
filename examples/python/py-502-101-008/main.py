
import logging
import traceback

logger = logging.getLogger(__name__)

def handle_request(request):
    try:
        return process_request(request)
    except Exception as e:
        request_id = getattr(request, "id", "unknown")
        user_id = getattr(request, "user_id", "anonymous")
        
        logger.error(
            "Unhandled exception during request processing",
            extra={
                "request_id": request_id,
                "user_id": user_id,
                "exception_type": type(e).__name__,
                "exception_message": str(e),
                "traceback": traceback.format_exc()
            }
        )
        raise
