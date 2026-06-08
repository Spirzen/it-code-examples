func loadConfig() throws -> [String: String] {
    let data = try Data(contentsOf: URL(fileURLWithPath: "/tmp/config.json"))
    let dict = try JSONSerialization.jsonObject(with: data) as? [String: String]
    guard let dict else { throw ParseError.notANumber("config") }
    return dict
}

func bootstrap() {
    do {
        let config = try loadConfig()
        print(config["apiBase"] ?? "default")
    } catch {
        print("Не удалось загрузить конфиг: \(error)")
    }
}
