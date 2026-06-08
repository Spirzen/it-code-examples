public class Config {
    private static String apiUrl;

    static {
        // Чтение конфигурации из файла или системы
        apiUrl = System.getenv("API_URL");
        if (apiUrl == null) {
            apiUrl = "https://default.api.com";
        }
    }

    public static String getApiUrl() {
        return apiUrl;
    }
}
