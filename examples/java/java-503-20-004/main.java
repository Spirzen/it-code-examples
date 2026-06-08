
import java.time.*;

public class PeriodDurationExample {
    public static void main(String[] args) {
        LocalDate birth = LocalDate.of(2010, 5, 15);
        LocalDate today = LocalDate.now();
        Period age = Period.between(birth, today);
        System.out.printf("Возраст: %d лет, %d месяцев, %d дней%n",
                age.getYears(), age.getMonths(), age.getDays());

        LocalDateTime start = LocalDateTime.of(2026, 2, 26, 9, 0);
        LocalDateTime end = start.plusHours(2).plusMinutes(45);
        Duration lesson = Duration.between(start, end);
        System.out.println("Длительность занятия: " + lesson.toMinutes() + " мин");

        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd.MM.yyyy HH:mm");
        System.out.println("Начало: " + start.format(fmt));
    }
}
