@RestController
@RequestMapping("/api/v1/orders")
@Tag(name = "Orders", description = "Order management operations")
public class OrderController {
    
    @Operation(summary = "Create a new order", 
               description = "Creates an order for authenticated customer")
    @ApiResponses(value = {
        @ApiResponse(responseCode = "201", description = "Order created",
            content = @Content(mediaType = "application/json",
                schema = @Schema(implementation = OrderResponse.class))),
        @ApiResponse(responseCode = "400", description = "Invalid request",
            content = @Content(mediaType = "application/json",
                schema = @Schema(implementation = ErrorResponse.class))),
        @ApiResponse(responseCode = "401", description = "Unauthorized")
    })
    @PostMapping
    public ResponseEntity<OrderResponse> createOrder(
        @io.swagger.v3.oas.annotations.parameters.RequestBody(
            description = "Order creation request", required = true,
            content = @Content(schema = @Schema(implementation = OrderRequest.class))
        )
        @Valid @RequestBody OrderRequest request
    ) {
        Order order = orderService.createOrder(request);
        URI location = ServletUriComponentsBuilder.fromCurrentRequest()
            .path("/{id}")
            .buildAndExpand(order.getId())
            .toUri();
        
        return ResponseEntity.created(location).body(toResponse(order));
    }
}
