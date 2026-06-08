try
{
    ProcessData();
}
catch (SpecificException ex)
{
    logger.LogWarning("Не критичная ошибка, продолжаем работу: {Message}", ex.Message);
    // Продолжаем работу с дефолтными значениями
}
