class SecureStorage {
    private var encryptionKey: String
    private var storage: [String: String] = [:]
    
    init(key: String) {
        self.encryptionKey = key
    }
    
    func store(key: String, value: String) {
        let encrypted = encrypt(value, with: encryptionKey)
        storage[key] = encrypted
    }
    
    func retrieve(key: String) -> String? {
        guard let encrypted = storage[key] else { return nil }
        return decrypt(encrypted, with: encryptionKey)
    }
    
    private func encrypt(_ value: String, with key: String) -> String {
        return value.reversed() + key
    }
    
    private func decrypt(_ value: String, with key: String) -> String {
        let length = value.count - key.count
        let index = value.index(value.startIndex, offsetBy: length)
        return String(value[..<index]).reversed()
    }
}
