public class Resource
{
    public int Id { get; set; }
    public void Use()
    {
        Console.WriteLine($"Resource {Id} is being used.");
    }
}
public class ObjectPool
{
    private readonly Stack<Resource> _available = new Stack<Resource>();
    private int _counter = 0;
    public Resource Get()
    {
        if (_available.Count == 0)
        {
            _counter++;
            return new Resource { Id = _counter };
        }

        return _available.Pop();
    }
    public void Release(Resource resource)
    {
        _available.Push(resource);
    }
}
