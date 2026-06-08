public class PaymentProcessor {
    
    public CompletableFuture<PaymentResult> processPaymentAsync(PaymentRequest request) {
        return CompletableFuture.supplyAsync(() -> validateRequest(request))
            .thenCompose(validatedRequest -> authorizePayment(validatedRequest))
            .thenCompose(authorization -> capturePayment(authorization))
            .thenApply(captureResult -> buildPaymentResult(captureResult))
            .exceptionally(ex -> handlePaymentError(ex, request));
    }
    
    private PaymentRequest validateRequest(PaymentRequest request) {
        if (request.getAmount().compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Amount must be positive");
        }
        return request;
    }
    
    private CompletableFuture<Authorization> authorizePayment(PaymentRequest request) {
        return paymentGateway.authorize(request);
    }
    
    private CompletableFuture<CaptureResult> capturePayment(Authorization auth) {
        return paymentGateway.capture(auth);
    }
}
