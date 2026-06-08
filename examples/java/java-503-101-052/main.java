@RestController
@RequestMapping("/orders")
public class OrderController {
    private final Tracer tracer;
    private final OrderService orderService;
    
    @PostMapping
    public ResponseEntity<OrderResponse> createOrder(@RequestBody OrderRequest request) {
        Span span = tracer.nextSpan().name("createOrder").start();
        
        try (Tracer.SpanInScope ws = tracer.withSpanInScope(span)) {
            span.tag("order.customerId", request.getCustomerId().toString());
            span.tag("order.itemsCount", String.valueOf(request.getItems().size()));
            
            Order order = orderService.createOrder(request);
            
            span.tag("order.id", order.getId().toString());
            return ResponseEntity.ok(toResponse(order));
        } catch (Exception e) {
            span.error(e);
            throw e;
        } finally {
            span.finish();
        }
    }
}
