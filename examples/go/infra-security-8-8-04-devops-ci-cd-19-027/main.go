func (s *OrderService) ProcessOrder(ctx context.Context, order *Order) error {
    ctx, span := tracer.Start(ctx, "order.process",
        trace.WithAttributes(
            // Идентификаторы
            attribute.String("order.id", order.ID),
            attribute.String("customer.id", order.CustomerID),
            
            // Бизнес-контекст
            attribute.Int("order.item_count", len(order.Items)),
            attribute.Float64("order.total_amount", order.TotalAmount),
            attribute.String("order.currency", order.Currency),
            attribute.String("payment.method", order.PaymentMethod),
            
            // Операционный контекст
            attribute.String("service.version", version),
            attribute.String("deployment.environment", env),
        ),
    )
    defer span.End()
    
    // Валидация с собственным span
    if err := s.validate(ctx, order); err != nil {
        span.RecordError(err)
        span.SetStatus(codes.Error, "validation_failed")
        return err
    }
    
    // Оплата с собственным span
    if err := s.charge(ctx, order); err != nil {
        span.RecordError(err)
        span.SetStatus(codes.Error, "payment_failed")
        return err
    }
    
    // Исполнение с собственным span
    if err := s.fulfill(ctx, order); err != nil {
        span.RecordError(err)
        span.SetStatus(codes.Error, "fulfillment_failed")
        return err
    }
    
    span.SetStatus(codes.Ok, "order_processed")
    return nil
}
