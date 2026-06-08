// Плохо: пустой catch
try
{
    ProcessData();
}
catch
{
    // Ничего не делаем
}

// Плохо: игнорирование результата
int.TryParse("invalid", out int result); // result = 0, но мы не знаем об ошибке
