@Aspect
@Component
public class ResilienceAspect {
    
    private final CircuitBreakerRegistry circuitBreakerRegistry;
    private final RetryRegistry retryRegistry;
    private final RateLimiterRegistry rateLimiterRegistry;
    private final TimeLimiterRegistry timeLimiterRegistry;
    
    @Around("@annotation(Resilient)")
    public Object resilientExecution(ProceedingJoinPoint joinPoint) throws Throwable {
        String operationName = joinPoint.getSignature().getName();
        
        // Построение цепочки защитных механизмов
        CircuitBreaker circuitBreaker = circuitBreakerRegistry.circuitBreaker(operationName);
        Retry retry = retryRegistry.retry(operationName);
        RateLimiter rateLimiter = rateLimiterRegistry.rateLimiter(operationName);
        TimeLimiter timeLimiter = timeLimiterRegistry.timeLimiter(operationName);
        
        // Декорирование операции всеми паттернами
        Supplier<Object> decoratedSupplier = Decorators.ofSupplier(() -> {
            try {
                return joinPoint.proceed();
            } catch (Throwable t) {
                throw new RuntimeException(t);
            }
        })
        .withCircuitBreaker(circuitBreaker)
        .withRetry(retry)
        .withRateLimiter(rateLimiter)
        .withFallback(Arrays.asList(TimeoutException.class, CallNotPermittedException.class),
            throwable -> getFallbackResponse(operationName, throwable))
        .decorate();
        
        // Ограничение времени выполнения
        return timeLimiter.executeFutureSupplier(
            () -> CompletableFuture.supplyAsync(decoratedSupplier::get)
        );
    }
    
    private Object getFallbackResponse(String operation, Throwable cause) {
        // Логирование и возврат запасного варианта
        log.warn("Fallback сработал для {}: {}", operation, cause.getMessage());
        return FallbackResponse.forOperation(operation);
    }
}
