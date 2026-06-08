public class ResourceLoader {
    
    public String loadTemplate(String templateName) throws IOException {
        URL resourceUrl = getClass().getClassLoader()
            .getResource("templates/" + templateName + ".html");
        
        if (resourceUrl == null) {
            throw new FileNotFoundException("Template not found: " + templateName);
        }
        
        return Files.readString(Path.of(resourceUrl.toURI()));
    }
    
    public Properties loadConfiguration() throws IOException {
        Properties properties = new Properties();
        try (InputStream input = getClass().getClassLoader()
                .getResourceAsStream("application.properties")) {
            if (input == null) {
                throw new FileNotFoundException("Configuration file not found");
            }
            properties.load(input);
        }
        return properties;
    }
}
