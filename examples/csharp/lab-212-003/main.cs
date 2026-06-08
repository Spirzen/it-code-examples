public class InventoryScene : Scene
{
    public override string Id => "inventory";
    public override string Description => "Ваш инвентарь пуст.";

    public override List<Choice> GetChoices(GameState state)
    {
        var description = state.Inventory.Count == 0
            ? "Ваш инвентарь пуст."
            : $"В инвентаре: {string.Join(", ", state.Inventory)}.";

        // Динамическое обновление описания
        _description = description;

        return new()
        {
            new Choice
            {
                Text = "Назад",
                TargetSceneId = state.CurrentSceneId == "inventory" ? "start" : state.CurrentSceneId
            }
        };
    }

    private string _description = string.Empty;
    public override string Description => _description;
}
