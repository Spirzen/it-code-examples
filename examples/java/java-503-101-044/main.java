public interface Specification<T> {
    Predicate toPredicate(Root<T> root, CriteriaQuery<?> query, CriteriaBuilder cb);
}

public class OrderSpecifications {
    public static Specification<OrderEntity> byCustomer(CustomerId customerId) {
        return (root, query, cb) -> 
            cb.equal(root.get("customerId"), customerId.value());
    }
    
    public static Specification<OrderEntity> pending() {
        return (root, query, cb) -> 
            cb.equal(root.get("status"), OrderStatus.PENDING.name());
    }
    
    public static Specification<OrderEntity> withAmountGreaterThan(BigDecimal amount) {
        return (root, query, cb) -> 
            cb.greaterThan(root.get("totalAmount"), amount);
    }
}

// Использование
List<Order> orders = orderRepository.findAll(
    Specification.where(OrderSpecifications.byCustomer(customerId))
                .and(OrderSpecifications.pending())
                .and(OrderSpecifications.withAmountGreaterThan(minAmount))
);
