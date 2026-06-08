// Плохо: устаревшие классы
public class OldEvent {
    private Date startDate;
    private Date endDate;
}

// Хорошо: современные классы
public class Event {
    private LocalDateTime startDateTime;
    private LocalDateTime endDateTime;
    private ZoneId timeZone;
    
    public boolean isHappeningNow() {
        LocalDateTime now = LocalDateTime.now(timeZone);
        return !now.isBefore(startDateTime) && now.isBefore(endDateTime);
    }
    
    public Duration getDuration() {
        return Duration.between(startDateTime, endDateTime);
    }
}
