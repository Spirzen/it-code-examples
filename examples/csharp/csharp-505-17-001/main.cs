bool TryParse(string input, out int result)
{
    if (int.TryParse(input, out result))
        return true;
    else
    {
        result = 0;
        return false;
    }
}

if (TryParse("123", out int value))
{
    Console.WriteLine(value); // 123
}
