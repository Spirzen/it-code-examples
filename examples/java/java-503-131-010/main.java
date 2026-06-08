
import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.UnknownHostException;

public class UrlChecker {
    public static void main(String[] args) {
        String urlString = "https://example.com";

        try {
            URL url = new URL(urlString);
            
            System.out.println("Анализ URL: " + urlString);
            System.out.println("Протокол: " + url.getProtocol());
            System.out.println("Хост: " + url.getHost());
            System.out.println("Порт: " + url.getPort());
            System.out.println("Путь: " + url.getPath());

            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("HEAD"); // HEAD запрос быстрее GET
            connection.setConnectTimeout(5000); // 5 секунд таймаут
            connection.connect();

            int statusCode = connection.getResponseCode();
            System.out.println("Статус кода: " + statusCode);

            if (statusCode >= 200 && statusCode < 300) {
                System.out.println("Ресурс доступен.");
            } else {
                System.out.println("Ресурс недоступен или вернул ошибку.");
            }

            connection.disconnect();

        } catch (UnknownHostException e) {
            System.out.println("Ошибка: Хост не найден.");
        } catch (IOException e) {
            System.out.println("Ошибка сети: " + e.getMessage());
        }
    }
}
