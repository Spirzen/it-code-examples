public class NumberSequence : IEnumerable<int>
{
    private readonly int _count;

    public NumberSequence(int count)
    {
        _count = count;
    }

    public IEnumerator<int> GetEnumerator()
    {
        return new NumberEnumerator(_count);
    }

    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
}

public class NumberEnumerator : IEnumerator<int>
{
    private readonly int _count;
    private int _current = -1;

    public NumberEnumerator(int count)
    {
        _count = count;
    }

    public int Current { get; private set; }

    object IEnumerator.Current => Current;

    public bool MoveNext()
    {
        _current++;
        if (_current >= _count)
            return false;
        Current = _current + 1;
        return true;
    }

    public void Reset() => _current = -1;

    public void Dispose() { }
}
