public class GameLoop
{
    private readonly Dictionary<string, Scene> _scenes = new();
    private readonly GameState _state = new();

    public GameLoop()
    {
        // Регистрация всех сцен
        RegisterScene(new StartScene());
        RegisterScene(new RedRoomScene());
        RegisterScene(new BlueRoomScene());
        RegisterScene(new InventoryScene());
        RegisterScene(new ChestScene());
        // .. другие сцены
    }

    private void RegisterScene(Scene scene)
    {
        _scenes[scene.Id] = scene;
    }

    public async Task RunAsync()
    {
        Narrator.Say("Добро пожаловать в текстовую игру!");
        Console.Write("Введите ваше имя: ");
        _state.PlayerName = (await Console.In.ReadLineAsync())?.Trim() ?? "Игрок";

        while (_state.Health > 0)
        {
            if (!_scenes.TryGetValue(_state.CurrentSceneId, out var currentScene))
            {
                Narrator.Say("Ошибка: неизвестная сцена. Игра завершена.");
                break;
            }

            Narrator.Say(currentScene.Description);
            var choices = currentScene.GetChoices(_state);
            Narrator.ShowChoices(choices);

            var selectedIndex = await PlayerInput.ReadChoiceAsync(choices.Count);
            var selectedChoice = choices[selectedIndex];

            // Выполнение действия при выборе
            selectedChoice.OnSelect?.Invoke(_state);

            // Переход к новой сцене
            _state.CurrentSceneId = selectedChoice.TargetSceneId;

            // Простая проверка завершения
            if (_state.CurrentSceneId == "end")
            {
                Narrator.Say($"Игра окончена! Ваш счёт: {_state.Score}");
                break;
            }
        }

        if (_state.Health <= 0)
        {
            Narrator.Say("Вы погибли. Игра окончена.");
        }
    }
}
