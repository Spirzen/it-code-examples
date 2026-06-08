// Имя тестового класса: <Имя класса>Test
public class OrderServiceTest {
    
    // Имя тестового метода: <метод>_<сценарий>_<результат>
    @Test
    public void calculateTotal_withDiscount_appliesDiscountCorrectly() {
        // arrange
        Order order = new Order();
        order.addItem(new OrderItem(product1, 2));
        order.addItem(new OrderItem(product2, 1));
        order.setDiscountCode("SUMMER20");
        
        // act
        BigDecimal total = order.calculateTotal();
        
        // assert
        assertEquals(new BigDecimal("240.00"), total);
    }
}
