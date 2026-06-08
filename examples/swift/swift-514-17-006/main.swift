func fetchWithRetry<T>(_ operation: @escaping () async throws -> T, maxAttempts: Int = 3) async throws -> T {
    var lastError: Error?
    for attempt in 1...maxAttempts {
        do {
            return try await operation()
        } catch {
            lastError = error
            if attempt < maxAttempts {
                let delay = pow(2.0, Double(attempt - 1))
                try await Task.sleep(for: .seconds(delay))
            }
        }
    }
    throw lastError!
}
