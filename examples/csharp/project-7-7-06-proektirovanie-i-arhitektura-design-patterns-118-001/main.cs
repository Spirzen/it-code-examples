public class NumberCollection : IEnumerable<int>
{
    private readonly int[] _items = { 1, 2, 3, 4, 5 };

    public IEnumerator<int> GetEnumerator()
        => new NumberEnumerator(_items);

    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
}

public class NumberEnumerator : IEnumerator<int>
{
    private readonly int[] _items;
    private int _position = -1;

    public NumberEnumerator(int[] items) => _items = items;

    public int Current => _items[_position];
    object IEnumerator.Current => Current;

    public bool MoveNext()
    {
        _position++;
        return _position < _items.Length;
    }

    public void Reset() => _position = -1;
    public void Dispose() { }
}
