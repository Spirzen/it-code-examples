@propertyWrapper
struct AppStorage<T> {
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

struct Settings {
    @AppStorage(key: "darkMode", defaultValue: false)
    static var isDarkMode: Bool

    @AppStorage(key: "fontScale", defaultValue: 1.0)
    static var fontScale: Double
}
