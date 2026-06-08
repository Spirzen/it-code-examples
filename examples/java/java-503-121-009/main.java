@ApplicationScoped
public class Service {

    @Inject
    @ConfigProperty(name = "app.name")
    String appName;

    @Inject
    @ConfigProperty(name = "app.ports")
    List<Integer> ports;

    @Inject
    @ConfigProperty(name = "app.enabled", defaultValue = "true")
    boolean enabled;

    @Inject
    @ConfigProperty(name = "app.timeout")
    Duration timeout; // "30s" → Duration.ofSeconds(30)
}
