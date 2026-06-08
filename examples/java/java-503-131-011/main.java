
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

public class DateConverter {
    public static void main(String[] args) {
        String dateString = "2026-05-06 14:30:00";
        String inputPattern = "yyyy-MM-dd HH:mm:ss";
        String outputPattern = "dd/MM/yyyy HH:mm";

        DateTimeFormatter inputFormatter = DateTimeFormatter.ofPattern(inputPattern);
        DateTimeFormatter outputFormatter = DateTimeFormatter.ofPattern(outputPattern);

        try {
            LocalDateTime dateTime = LocalDateTime.parse(dateString, inputFormatter);
            
            // Конвертация в другой формат
            String formattedDate = dateTime.format(outputFormatter);
            
            System.out.println("Исходная строка: " + dateString);
            System.out.println("Преобразованная строка: " + formattedDate);
            
            // Пример получения даты сегодня
            LocalDate today = LocalDate.now();
            System.out.println("Сегодня: " + today);

        } catch (DateTimeParseException e) {
            System.out.println("Неверный формат даты: " + e.getMessage());
        }
    }
}
