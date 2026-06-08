public static class Narrator
{
    public static void Say(string message)
    {
        Console.WriteLine($"\n{message}\n");
    }

    public static void ShowChoices(List<Choice> choices)
    {
        for (int i = 0; i < choices.Count; i++)
        {
            Console.WriteLine($"{i + 1}. {choices[i].Text}");
        }
    }
}
