public interface IMovable
{
    void Move();
}

public class Car : IMovable
{
    public void Move() => Drive();
    private void Drive() => Console.WriteLine("Car is driving.");
}

public class Camel
{
    public void Walk() => Console.WriteLine("Camel is walking.");
}

public class CamelAdapter : IMovable
{
    private readonly Camel _camel;

    public CamelAdapter(Camel camel) => _camel = camel;

    public void Move() => _camel.Walk();
}
