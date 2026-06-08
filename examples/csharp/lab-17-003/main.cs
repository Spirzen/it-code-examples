using Система;
using Система.IO;
using ClosedXML.Excel;

public class RobustExcelParser
{
    public static void ParseAllSheets(string filePath)
    {
        if (!File.Exists(filePath))
        {
            Console.WriteLine($"Файл не найден: {filePath}");
            return;
        }

        try
        {
            using var workbook = new XLWorkbook(filePath);

            foreach (var worksheet in workbook.Worksheets)
            {
                Console.WriteLine($"\n--- Лист: {worksheet.Name} ---");

                var range = worksheet.RangeUsed();
                if (range == null) continue;

                foreach (var row in range.Rows())
                {
                    var line = string.Join(" | ", row.CellsSelect(c => c.Value?.ToString() ?? "[пусто]"));
                    Console.WriteLine(line);
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка при чтении файла: {ex.Message}");
        }
    }
}
