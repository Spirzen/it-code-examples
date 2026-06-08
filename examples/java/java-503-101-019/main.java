@Test
public void processPayment_validCard_chargesAmount() {
    // arrange
    PaymentService paymentService = new PaymentService(gatewayMock);
    Payment payment = new Payment("4111111111111111", BigDecimal.valueOf(100.00));
    
    // act
    PaymentResult result = paymentService.process(payment);
    
    // assert
    assertTrue(result.isSuccess());
    assertEquals("Payment approved", result.getMessage());
    verify(gatewayMock).charge(eq(payment.getAmount()));
}
