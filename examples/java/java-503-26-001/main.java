public class Example implements Serializable {
    private String username;           // поле
    private boolean loggedIn;          // поле
    private URL endpoint;              // поле
    private final String id = UUID.randomUUID().toString(); // final-поле

    public Example() {}

    // ✅ Корректное свойство 'username'
    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }

    // ✅ Корректное булево свойство 'loggedIn' с is-геттером
    public boolean isLoggedIn() { return loggedIn; }
    public void setLoggedIn(boolean loggedIn) { this.loggedIn = loggedIn; }

    // ✅ Корректное свойство 'endpoint' — первые две буквы заглавные, сохраняются
    public URL getEndpoint() { return endpoint; }
    public void setEndpoint(URL endpoint) { this.endpoint = endpoint; }

    // ⚠️ Поле 'id' не является свойством — нет сеттера, и геттер, если бы был,
    //    не позволял бы изменение. Это не нарушает JavaBean, но делает поле
    //    "невидимым" для интроспекции как изменяемое свойство.
    public String getId() { return id; } // только чтение — read-only property
}
