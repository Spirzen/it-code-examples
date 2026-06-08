public class SchedulerService {
    private static final ZoneId DEFAULT_ZONE = ZoneId.of("Europe/Moscow");
    
    public void scheduleNotification(User user, LocalDateTime localTime) {
        // Преобразование локального времени пользователя в UTC
        ZonedDateTime userDateTime = localTime.atZone(user.getTimeZone());
        ZonedDateTime utcDateTime = userDateTime.withZoneSameInstant(ZoneOffset.UTC);
        
        notificationScheduler.schedule(utcDateTime.toInstant(), user.getId());
    }
    
    public String formatForUser(LocalDateTime utcTime, User user) {
        ZonedDateTime userTime = utcTime.atZone(ZoneOffset.UTC)
                                       .withZoneSameInstant(user.getTimeZone());
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd.MM.yyyy HH:mm");
        return userTime.format(formatter);
    }
}
