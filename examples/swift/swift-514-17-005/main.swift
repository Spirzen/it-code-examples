func loadImage(for url: URL) async throws -> UIImage {
    if let image = memoryCache[url] { return image }
    if let image = try diskCache.loadImage(for: url) {
        memoryCache[url] = image
        return image
    }
    let data = try await URLSession.shared.data(from: url).0
    guard let image = UIImage(data: data) else {
        throw NetworkError.invalidImageData
    }
    memoryCache[url] = image
    try diskCache.save(image, for: url)
    return image
}
