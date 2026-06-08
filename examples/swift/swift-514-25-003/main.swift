@propertyWrapper
struct Storage<T> {
    let key: String
    let defaultValue: T

    var wrappedValue: T {
        get {
            UserDefaults.standard.object(forKey: key) as? T ?? defaultValue
        }
        set {
            UserDefaults.standard.set(newValue, forKey: key)
        }
    }
}

struct AppSettings {
    @Storage(key: "darkMode", defaultValue: false)
    static var isDarkMode: Bool
}
