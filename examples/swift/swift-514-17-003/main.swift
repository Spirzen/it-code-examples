extension NSManagedObjectContext {
    func perform<T>(_ block: @escaping (NSManagedObjectContext) async throws -> T) async throws -> T {
        return try await withCheckedThrowingContinuation { continuation in
            self.perform {
                Task {
                    do {
                        let result = try await block(self)
                        continuation.resume(returning: result)
                    } catch {
                        continuation.resume(throwing: error)
                    }
                }
            }
        }
    }
}
