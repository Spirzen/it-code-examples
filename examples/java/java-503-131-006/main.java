
import java.io.*;
import java.net.*;

public class RestApiClient {
    public static void main(String[] args) throws IOException {
        String apiUrl = "https://jsonplaceholder.typicode.com/posts";
        String jsonInput = "{ \"title\": \"foo\", \"body\": \"bar\", \"userId\": 1 }";

        URL url = new URL(apiUrl);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();

        conn.setDoOutput(true);
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "application/json");

        try (OutputStream os = conn.getOutputStream()) {
            byte[] input = jsonInput.getBytes("utf-8");
            os.write(input, 0, input.length);
        }

        int responseCode = conn.getResponseCode();
        System.out.println("Отправлен запрос. Код ответа: " + responseCode);

        if (responseCode == HttpURLConnection.HTTP_CREATED) {
            System.out.println("Ресурс успешно создан.");
        }

        conn.disconnect();
    }
}
