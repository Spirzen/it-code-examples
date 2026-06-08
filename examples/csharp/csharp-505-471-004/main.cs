public readonly struct MyValueTaskSource : IValueTaskSource<int>
{
    private ManualResetValueTaskSourceCore<int> _core;

    public ValueTask<int> GetValueAsync()
    {
        var vt = new ValueTask<int>(this, _core.Version);
        // ... запуск операции, по завершении: _core.SetResult(value)
        return vt;
    }

    // Реализация IValueTaskSource<int>:
    public int GetResult(short token) => _core.GetResult(token);
    public ValueTaskSourceStatus GetStatus(short token) => _core.GetStatus(token);
    public void OnCompleted(Action<object?> continuation, object? state, short token, ValueTaskSourceOnCompletedFlags flags)
        => _core.OnCompleted(continuation, state, token, flags);
}
