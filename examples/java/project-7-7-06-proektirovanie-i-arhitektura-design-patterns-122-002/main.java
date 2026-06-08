public class AuthenticationHandler extends RequestHandler {
    @Override
    public void handle(HttpRequest request) {
        if (request.getToken() == null) {
            throw new SecurityException("Нет токена");
        }
        System.out.println("Аутентификация пройдена");
        super.handle(request);
    }
}

public class RateLimitHandler extends RequestHandler {
    private final Map<String, Integer> counters = new ConcurrentHashMap<>();

    @Override
    public void handle(HttpRequest request) {
        int count = counters.merge(request.getIp(), 1, Integer::sum);
        if (count > 100) {
            throw new RuntimeException("429 Too Many Requests");
        }
        System.out.println("Rate limit OK");
        super.handle(request);
    }
}

public class BusinessLogicHandler extends RequestHandler {
    @Override
    public void handle(HttpRequest request) {
        System.out.println("Бизнес-логика выполнена");
    }
}
