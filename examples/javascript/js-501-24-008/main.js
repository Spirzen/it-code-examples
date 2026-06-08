window.addEventListener('error', function(event) {
    const errorInfo = {
        message: event.message,
        filename: event.filename,
        lineno: event.lineno,
        colno: event.colno,
        stack: event.error?.stack,
        timestamp: new Date().toISOString(),
        userAgent: navigator.userAgent,
        url: window.location.href
    };
    
    sendErrorToServer(errorInfo);
    return false;
});

window.addEventListener('unhandledrejection', function(event) {
    const errorInfo = {
        reason: event.reason,
        stack: event.reason?.stack,
        timestamp: new Date().toISOString(),
        url: window.location.href
    };
    
    sendErrorToServer(errorInfo);
    event.preventDefault();
});
