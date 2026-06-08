[AttributeUsage(
    AttributeTargets.Class | AttributeTargets.Method,
    AllowMultiple = false,
    Inherited = true)]
public sealed class MyAttribute : Attribute
{
    public string Name { get; }
    public int Priority { get; set; } = 0;

    public MyAttribute(string name)
    {
        Name = name ?? throw new ArgumentNullException(nameof(name));
    }
}
