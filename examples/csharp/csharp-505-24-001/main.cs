public (bool Success, string Message, int Code) Validate(string input)
{
    if (string.IsNullOrWhiteSpace(input))
        return (false, "Input is empty", 400);

    return (true, "OK", 200);
}

// Использование:
var result = Validate("test");
if (result.Success)
{
    Console.WriteLine(result.Message);
}
