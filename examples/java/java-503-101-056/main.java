public class User {
    private final LocalDate birthDate;
    
    public int getAge() {
        return Period.between(birthDate, LocalDate.now()).getYears();
    }
    
    public boolean isAdult() {
        return getAge() >= 18;
    }
    
    public boolean hasBirthdayToday() {
        LocalDate today = LocalDate.now();
        return birthDate.getMonth() == today.getMonth() 
            && birthDate.getDayOfMonth() == today.getDayOfMonth();
    }
}
