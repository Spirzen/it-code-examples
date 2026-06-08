// Проблема: спан без контекстных атрибутов
func (s *OrderService) ProcessOrder(ctx context.Context, order *Order) error {
    ctx, span := tracer.Start(ctx, "process_order")
    defer span.End()
    
    // Спан содержит только имя и время
    // Отсутствуют: order_id, customer_id, item_count, total_amount
    
    if err := s.validate(ctx, order); err != nil {
        return err
    }
    
    if err := s.charge(ctx, order); err != nil {
        return err
    }
    
    return s.fulfill(ctx, order)
}
