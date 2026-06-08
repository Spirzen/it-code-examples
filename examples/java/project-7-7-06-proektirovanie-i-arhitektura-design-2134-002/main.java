public class CircuitBreaker {
    public enum State { CLOSED, OPEN, HALF_OPEN }
    
    private State state = State.CLOSED;
    private int failureCount = 0;
    private final int failureThreshold;
    private final Duration resetTimeout;
    private Instant lastFailureTime;
    
    public CircuitBreaker(int failureThreshold, Duration resetTimeout) {
        this.failureThreshold = failureThreshold;
        this.resetTimeout = resetTimeout;
    }
    
    public <T> T execute(Supplier<T> operation) {
        if (state == State.OPEN) {
            if (Instant.now().isAfter(lastFailureTime.plus(resetTimeout))) {
                state = State.HALF_OPEN;
            } else {
                throw new CircuitBreakerOpenException("Выключатель разомкнут");
            }
        }
        
        try {
            T result = operation.get();
            onSuccess();
            return result;
        } catch (Exception e) {
            onFailure();
            throw e;
        }
    }
    
    private void onSuccess() {
        failureCount = 0;
        state = State.CLOSED;
    }
    
    private void onFailure() {
        failureCount++;
        lastFailureTime = Instant.now();
        if (failureCount >= failureThreshold) {
            state = State.OPEN;
        }
    }
}
