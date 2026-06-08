@RestController
@RequestMapping("/actuator")
public class HealthController {
    private final DataSource dataSource;
    private final CacheManager cacheManager;
    private final ExternalService externalService;
    
    @GetMapping("/health")
    public ResponseEntity<HealthResponse> health() {
        HealthStatus dbStatus = checkDatabase();
        HealthStatus cacheStatus = checkCache();
        HealthStatus externalStatus = checkExternalService();
        
        HealthStatus overall = determineOverallStatus(dbStatus, cacheStatus, externalStatus);
        
        HealthResponse response = new HealthResponse(
            overall,
            Map.of(
                "database", dbStatus,
                "cache", cacheStatus,
                "externalService", externalStatus
            ),
            Instant.now()
        );
        
        HttpStatus status = overall == HealthStatus.UP ? HttpStatus.OK : HttpStatus.SERVICE_UNAVAILABLE;
        return ResponseEntity.status(status).body(response);
    }
    
    private HealthStatus checkDatabase() {
        try {
            try (Connection conn = dataSource.getConnection();
                 Statement stmt = conn.createStatement();
                 ResultSet rs = stmt.executeQuery("SELECT 1")) {
                return HealthStatus.UP;
            }
        } catch (Exception e) {
            return HealthStatus.DOWN;
        }
    }
}
