@Service
public class OrderService {

    @Transactional
    public Order createOrder(Long userId, List<OrderItem> items) {
        User user = userRepository.findById(userId)
            .orElseThrow(() -> new EntityNotFoundException("User not found"));

        Order order = new Order();
        order.setUser(user);
        order.setItems(items);
        order.setStatus(OrderStatus.CREATED);
        order = orderRepository.save(order); // flush происходит автоматически

        paymentService.charge(user, order.getTotal()); // вызов другого @Transactional-метода
        return order;
    }
}
