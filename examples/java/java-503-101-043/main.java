// Доменный интерфейс
public interface OrderRepository {
    Order findById(OrderId id);
    List<Order> findByCustomer(CustomerId customerId);
    List<Order> findPendingOrders();
    void save(Order order);
    void delete(OrderId id);
}

// Инфраструктурная реализация
@Repository
public class JpaOrderRepository implements OrderRepository {
    private final JpaRepository<OrderEntity, Long> jpaRepository;
    
    @Override
    public Order findById(OrderId id) {
        return jpaRepository.findById(id.value())
            .map(this::toDomain)
            .orElse(null);
    }
    
    @Override
    public void save(Order order) {
        OrderEntity entity = toEntity(order);
        jpaRepository.save(entity);
        order.markEventsAsCommitted();
    }
    
    private Order toDomain(OrderEntity entity) {
        // преобразование entity → domain object
    }
    
    private OrderEntity toEntity(Order order) {
        // преобразование domain object → entity
    }
}
