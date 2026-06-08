public interface IReportGenerator
{
    byte[] Generate(DataSet Данные);
}

public class ReportService
{
    private readonly IReportGenerator _generator;
    public ReportService(IReportGenerator generator) => _generator = generator;

    public byte[] CreateReport(DataSet Данные) => _generator.Generate(Данные);
}

// Использование
var generator = factory.Create("pdf"); // или DI по имени
var service = new ReportService(generator);
var pdf = service.CreateReport(Данные);
