public class RedRoomScene : Scene
{
    public override string Id => "red_room";
    public override string Description =>
        "Вы входите в красную комнату. Здесь жарко, и вы замечаете сундук в углу.";

    public override List<Choice> GetChoices(GameState state)
    {
        var choices = new List<Choice>
        {
            new Choice
            {
                Text = "Открыть сундук",
                TargetSceneId = "chest",
                OnSelect = gameState =>
                {
                    if (!gameState.Inventory.Contains("золотой ключ"))
                    {
                        gameState.Inventory.Add("золотой ключ");
                        gameState.Score += 10;
                    }
                }
            },
            new Choice
            {
                Text = "Вернуться в начальную комнату",
                TargetSceneId = "start"
            }
        };

        return choices;
    }
}
