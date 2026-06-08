// File: DataProcessor.swift

fileprivate struct ParserState {
    var position: Int = 0
    var buffer: [Character] = []
    
    mutating func advance() {
        position += 1
    }
    
    func current() -> Character? {
        guard position < buffer.count else { return nil }
        return buffer[position]
    }
}

fileprivate func validateFormat(_ data: String) -> Bool {
    return !data.isEmpty && data.count <= 1000
}

fileprivate func normalizeData(_ data: String) -> String {
    return data.trimmingCharacters(in: .whitespacesAndNewlines)
}

class DataProcessor {
    func process(_ rawData: String) -> String {
        guard validateFormat(rawData) else {
            return ""
        }
        
        let normalized = normalizeData(rawData)
        var state = ParserState()
        state.buffer = Array(normalized)
        
        // Обработка данных
        return normalized
    }
}
