import java.util.HashMap;
import java.util.Map;

public final class HttpClient {
    private final String baseUrl;
    private final int connectTimeout;
    private final int readTimeout;
    private final Map<String, String> headers;
    private final int maxRetries;

    private HttpClient(Builder builder) {
        this.baseUrl = builder.baseUrl;
        this.connectTimeout = builder.connectTimeout;
        this.readTimeout = builder.readTimeout;
        this.headers = Map.copyOf(builder.headers);
        this.maxRetries = builder.maxRetries;
    }

    public static final class Builder {
        private final String baseUrl;
        private int connectTimeout = 5_000;
        private int readTimeout = 10_000;
        private Map<String, String> headers = new HashMap<>();
        private int maxRetries = 3;

        public Builder(String baseUrl) {
            this.baseUrl = baseUrl;
        }

        public Builder connectTimeout(int ms) {
            this.connectTimeout = ms;
            return this;
        }

        public Builder readTimeout(int ms) {
            this.readTimeout = ms;
            return this;
        }

        public Builder header(String key, String value) {
            this.headers.put(key, value);
            return this;
        }

        public Builder maxRetries(int retries) {
            this.maxRetries = retries;
            return this;
        }

        public HttpClient build() {
            if (baseUrl == null || baseUrl.isBlank()) {
                throw new IllegalArgumentException("baseUrl обязателен");
            }
            return new HttpClient(this);
        }
    }
}
