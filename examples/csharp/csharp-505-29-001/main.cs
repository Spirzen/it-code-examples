public static class LinqExtensions
{
    public static IEnumerable<T> SkipLast<T>(this IEnumerable<T> source, int count)
    {
        var buffer = new Queue<T>();
        foreach (var item in source)
        {
            buffer.Enqueue(item);
            if (buffer.Count > count)
                yield return buffer.Dequeue();
        }
    }
}

// Использование
var allButLastThree = numbers.SkipLast(3);
