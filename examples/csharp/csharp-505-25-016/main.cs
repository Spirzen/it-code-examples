public static class MathHelper
{
    public static double Pi => 3.14159;

    public static double CircleArea(double radius)
    {
        return Pi * radius * radius;
    }

    public static int Factorial(int n)
    {
        return n <= 1 ? 1 : n * Factorial(n - 1);
    }
}
