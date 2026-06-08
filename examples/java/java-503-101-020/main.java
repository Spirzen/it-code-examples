@Test
public void withdraw_amountEqualToBalance_succeeds() {
    Account account = new Account(BigDecimal.valueOf(1000.00));
    
    account.withdraw(BigDecimal.valueOf(1000.00));
    
    assertEquals(BigDecimal.ZERO, account.getBalance());
}

@Test
public void withdraw_amountGreaterThanBalance_throwsException() {
    Account account = new Account(BigDecimal.valueOf(1000.00));
    
    assertThrows(InsufficientFundsException.class, () -> {
        account.withdraw(BigDecimal.valueOf(1000.01));
    });
}

@Test
public void withdraw_negativeAmount_throwsException() {
    Account account = new Account(BigDecimal.valueOf(1000.00));
    
    assertThrows(IllegalArgumentException.class, () -> {
        account.withdraw(BigDecimal.valueOf(-100.00));
    });
}
