private sealed class HiddenClassForLambda
{
    public int aVariable;

    public void HiddenMethodForLambda(object? sender, System.Timers.ElapsedEventArgs args)
    {
        Console.WriteLine(aVariable);
    }
}

public void InitTimer()
{
    var hiddenObject = new HiddenClassForLambda();
    hiddenObject.aVariable = 5;
    _timer = new System.Timers.Timer(1000);
    _timer.Elapsed += hiddenObject.HiddenMethodForLambda;
    _timer.Enabled = true;
}
