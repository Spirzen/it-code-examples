public static class PlayerInput
{
    public static async Task<int> ReadChoiceAsync(int maxOptions)
    {
        while (true)
        {
            Console.Write("\nВаш выбор (введите номер): ");
            var input = await Console.In.ReadLineAsync();

            if (int.TryParse(input, out int choice) && choice >= 1 && choice <= maxOptions)
                return choice - 1; // индексация с нуля

            Console.WriteLine("Неверный ввод. Попробуйте снова.");
        }
    }
}
