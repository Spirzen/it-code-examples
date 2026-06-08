@ExtendWith(MockitoExtension.class)
public class OrderServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @Mock
    private OrderRepository orderRepository;
    
    @Mock
    private NotificationService notificationService;
    
    @InjectMocks
    private OrderService orderService;
    
    @Test
    public void placeOrder_validOrder_savesAndNotifies() {
        // arrange
        User user = new User(1L, "user@example.com");
        Order order = new Order(user, items);
        
        when(userRepository.findById(1L)).thenReturn(Optional.of(user));
        doNothing().when(notificationService).sendOrderConfirmation(any());
        
        // act
        Order result = orderService.placeOrder(order);
        
        // assert
        assertNotNull(result.getId());
        verify(orderRepository).save(order);
        verify(notificationService).sendOrderConfirmation(order);
    }
}
