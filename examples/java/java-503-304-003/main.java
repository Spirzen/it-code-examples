@Configuration
class StorageConfig {
    @Bean
    @Profile("dev")
    Storage localStorage() {
        return new LocalStorage();
    }

    @Bean
    @Profile("prod")
    Storage s3Storage() {
        return new S3Storage();
    }
}
