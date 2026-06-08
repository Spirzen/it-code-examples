HttpClient client = HttpClient.newBuilder()
    .build();

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://httpbin.org/get"))
    .header("User-Agent", "Debug")
    .GET()
    .build();

HttpResponse<String> response = client.send(request, BodyHandlers.ofString());

System.out.println("Status: " + response.statusCode());
System.out.println("Headers: " + response.headers().map());
System.out.println("Body: " + response.body());
