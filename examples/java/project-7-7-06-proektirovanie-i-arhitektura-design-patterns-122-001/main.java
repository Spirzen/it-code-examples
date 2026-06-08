public abstract class RequestHandler {
    private RequestHandler next;

    public RequestHandler setNext(RequestHandler next) {
        this.next = next;
        return next;
    }

    public void handle(HttpRequest request) {
        if (next != null) {
            next.handle(request);
        }
    }
}
