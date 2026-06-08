func fetchData() async throws -> Data {
    let (data, _) = try await URLSession.shared.data(from: url)
    return data
}

actor DataManager {
    private var cache: [String: Data] = [:]
    
    func cachedData(for key: String) -> Data? {
        return cache[key]
    }
    
    func store(_ data: Data, for key: String) {
        cache[key] = data
    }
}
