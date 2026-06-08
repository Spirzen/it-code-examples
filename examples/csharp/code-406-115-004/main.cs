public void ProcessOrder(Order order)
{
    ValidateOrder(order);
    // SaveOrder(order);  // Закомментировано 2023-05-15, не нужно временно
    // SendConfirmation(order);  // Закомментировано 2023-05-15
    // LogToLegacySystem(order);  // Старая система, убрать позже
    NotifyCustomer(order);
}
