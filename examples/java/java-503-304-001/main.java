public interface Notifier {
    void send(String message);
}

@Component("emailNotifier")
class EmailNotifier implements Notifier {
    public void send(String message) {}
}

@Component
class AlertService {
    private final Notifier notifier;

    public AlertService(@Qualifier("emailNotifier") Notifier notifier) {
        this.notifier = notifier;
    }
}
