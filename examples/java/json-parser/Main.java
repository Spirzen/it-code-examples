public class Main {
    public static void main(String[] args) {
        String json = """
            {
              "name": "Тимур",
              "age": 30,
              "active": true,
              "tags": ["Java", "JSON", "Parser"],
              "meta": {
                "score": 9.87e-3,
                "nullField": null
              }
            }
            """;

        JsonValue parsed = Json.parse(json);
        System.out.println("Name: " + parsed.asObject().get("name").asString());
        System.out.println("Round-trip:\n" + Json.stringify(parsed));
    }
}
