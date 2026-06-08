public class Calculator
{
    public int AddAndDouble(int a, int b)
    {
        int sum = Add(a, b);         // Работает, хотя Add объявлен ниже
        return Double(sum);          // Double тоже ниже
    }

    private int Add(int x, int y)
    {
        return x + y;
    }

    private int Double(int value)
    {
        return value * 2;
    }
}
