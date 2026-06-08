// C# (хороший пример)
public interface IPrinter
{
    void Print(string document);
}

public interface IScanner
{
    string Scan(string document);
}

public interface IFax
{
    void Fax(string document);
}

public class SimplePrinter : IPrinter
{
    public void Print(string document)
    {
        Console.WriteLine($"Printing: {document}");
    }
}

public class AllInOneDevice : IPrinter, IScanner, IFax
{
    public void Print(string document) => Console.WriteLine($"Printing: {document}");
    public string Scan(string document) => $"Scanned: {document}";
    public void Fax(string document) => Console.WriteLine($"Faxing: {document}");
}
