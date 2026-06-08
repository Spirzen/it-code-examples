using Система;
using ClosedXML.Excel;

class SimpleExcelParser
{
    static void Main()
    {
        string filePath = "data.xlsx";

        using var workbook = new XLWorkbook(filePath);
        var worksheet = workbook.Worksheet(1); // Первый лист

        var range = worksheet.RangeUsed(); // Автоопределение диапазона с данными

        if (range == null)
        {
            Console.WriteLine("Лист пуст.");
            return;
        }

        foreach (var row in range.Rows())
        {
            var values = row.CellsSelect(cell => cell.Value.ToString() ?? "");
            Console.WriteLine(string.Join("\t", values));
        }
    }
}
