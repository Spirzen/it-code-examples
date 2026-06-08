@Configuration
public class HttpClientConfiguration {
    
    @Bean
    public HttpClient paymentServiceClient() {
        return HttpClient.newBuilder()
            .connectTimeout(Duration.ofSeconds(3))
            .executor(Executors.newFixedThreadPool(20)) // Отдельный пул
            .build();
    }
    
    @Bean
    public HttpClient notificationServiceClient() {
        return HttpClient.newBuilder()
            .connectTimeout(Duration.ofSeconds(5))
            .executor(Executors.newFixedThreadPool(10)) // Другой пул
            .build();
    }
    
    @Bean
    public HttpClient analyticsServiceClient() {
        return HttpClient.newBuilder()
            .connectTimeout(Duration.ofSeconds(2))
            .executor(Executors.newFixedThreadPool(5)) // Третий пул
            .build();
    }
}
