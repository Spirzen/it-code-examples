enum ValidationError: Error { case empty }

let rawNickname: String? = "  tim  "

if let nick = rawNickname?.trimmingCharacters(in: .whitespacesAndNewlines), !nick.isEmpty {
    print("Привет, \(nick)")
}

func requireNickname(_ value: String?) throws -> String {
    guard let nick = value?.trimmingCharacters(in: .whitespacesAndNewlines), !nick.isEmpty else {
        throw ValidationError.empty
    }
    return nick
}

Разбор:
- `if let` с несколькими условиями через запятую: распаковка optional и проверка, что строка не пустая.
- Optional chaining `rawNickname?....` не выполняется, если `rawNickname == nil`.
- `guard let` в `requireNickname` обеспечивает ранний выход с `throw`, если данные невалидны.
- После `guard` компилятор считает `nick` не-optional `String` в оставшейся части функции.

---

### `if case let` — один случай без полного switch

Когда интересен **один** вариант:

