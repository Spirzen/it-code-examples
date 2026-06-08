struct Quote: Decodable { let text: String }

@MainActor
func showQuote(on label: UILabel) async {
    guard let url = URL(string: "https://api.example.com/quote") else { return }
    do {
        let (data, _) = try await URLSession.shared.data(from: url)
        let quote = try JSONDecoder().decode(Quote.self, from: data)
        label.text = quote.text
    } catch {
        label.text = "Ошибка загрузки"
    }
}

// Запуск с экрана:
Task { await showQuote(on: titleLabel) }
