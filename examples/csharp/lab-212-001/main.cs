public class StartScene : Scene
{
    public override string Id => "start";
    public override string Description => 
        "Вы просыпаетесь в тёмной комнате. Перед вами две двери: одна красная, другая синяя.";

    public override List<Choice> GetChoices(GameState state)
    {
        return new()
        {
            new Choice
            {
                Text = "Открыть красную дверь",
                TargetSceneId = "red_room"
            },
            new Choice
            {
                Text = "Открыть синюю дверь",
                TargetSceneId = "blue_room"
            },
            new Choice
            {
                Text = "Посмотреть инвентарь",
                TargetSceneId = "inventory"
            }
        };
    }
}
