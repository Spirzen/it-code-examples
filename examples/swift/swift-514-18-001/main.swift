func fetchData(from url: URL) async throws -> Data {
    let (data, _) = try await URLSession.shared.data(from: url)
    return data
}

// Вызов
Task {
    do {
        let data = try await fetchData(from: someURL)
        // Обработка данных
    } catch {
        // Обработка ошибки
    }
}
