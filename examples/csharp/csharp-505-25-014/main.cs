public class Counter
{
    private static int _totalCount = 0;
    public int InstanceId { get; }

    public Counter()
    {
        InstanceId = ++_totalCount;
    }

    public static int GetTotalCount() => _totalCount;
}
var c1 = new Counter(); // InstanceId = 1
var c2 = new Counter(); // InstanceId = 2
Console.WriteLine(Counter.GetTotalCount()); // 2
