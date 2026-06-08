@SpringBootApplication
public class Application implements ApplicationRunner {
    
    @Autowired
    private DataSource dataSource;
    
    @Autowired
    private CacheManager cacheManager;
    
    @Autowired
    private ReferenceDataService referenceDataService;
    
    @Override
    public void run(ApplicationArguments args) {
        // Прогрев пула соединений
        warmupConnectionPool();
        
        // Предзагрузка справочников
        preloadReferences();
        
        // Прогрев кэшей
        warmupCaches();
        
        // Форсирование JIT-компиляции
        warmupHotPaths();
    }
    
    private void warmupConnectionPool() {
        try (Connection conn = dataSource.getConnection()) {
            // Выполнение тестового запроса
            try (PreparedStatement stmt = conn.prepareStatement("SELECT 1")) {
                stmt.execute();
            }
        }
    }
    
    private void preloadReferences() {
        referenceDataService.loadCountries();
        referenceDataService.loadCurrencies();
        referenceDataService.loadCategories();
    }
}
