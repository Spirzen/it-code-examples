using Система;
using Система.Collections.Generic;
using Система.Globalization;
using ClosedXML.Excel;

public static class TypedExcelParser
{
    public static List<Employee> ParseEmployees(string filePath)
    {
        var employees = new List<Employee>();

        using var workbook = new XLWorkbook(filePath);
        var worksheet = workbook.Worksheet(1);
        var rows = worksheet.RangeUsedRowsUsed();

        // Пропускаем первую строку (заголовки)
        bool firstRow = true;
        foreach (var row in rows)
        {
            if (firstRow)
            {
                firstRow = false;
                continue;
            }

            var cells = row.CellsToList();
            if (cells.Count < 4) continue; // Защита от неполных строк

            var emp = new Employee
            {
                FullName = cells[0].Value?.ToString() ?? "",
                Department = cells[1].Value?.ToString() ?? ""
            };

            // Парсинг числа
            if (int.TryParse(cells[2].Value?.ToString out int salary))
                emp.Salary = salary;

            // Парсинг даты
            if (DateTime.TryParse(cells[3].Value?.ToString out DateTime hireDate))
                emp.HireDate = hireDate;

            employees.Add(emp);
        }

        return employees;
    }
}

// Использование
class Program
{
    static void Main()
    {
        var employees = TypedExcelParser.ParseEmployees("employees.xlsx");
        foreach (var emp in employees)
        {
            Console.WriteLine($"{emp.FullName}, {emp.Department}, {emp.Salary} руб., принят: {emp.HireDate:yyyy-MM-dd}");
        }
    }
}
