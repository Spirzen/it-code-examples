enum ParseError: Error {
    case emptyInput
    case notANumber(String)
}

func parseAge(from text: String) throws -> Int {
    let trimmed = text.trimmingCharacters(in: .whitespacesAndNewlines)
    guard !trimmed.isEmpty else { throw ParseError.emptyInput }
    guard let value = Int(trimmed) else { throw ParseError.notANumber(trimmed) }
    return value
}

func run() {
    do {
        let age = try parseAge(from: " 31 ")
        print("Возраст: \(age)")
    } catch ParseError.emptyInput {
        print("Строка пустая")
    } catch ParseError.notANumber(let raw) {
        print("Не число: \(raw)")
    } catch {
        print("Неизвестная ошибка: \(error)")
    }
}
