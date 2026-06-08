public class Example
{
    public void Method()
    {
        int unused = 42;  // Предупреждение: переменная не используется
        int x = 10;
        x = x + 1;        // Предупреждение: выражение можно упростить до x++
    }
}
