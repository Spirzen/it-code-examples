// Проверка версии приложения
func checkAppVersion() {
    let bundle = Bundle.main
    let version = bundle.object(forInfoDictionaryKey: "CFBundleShortVersionString") as? String
    let build = bundle.object(forInfoDictionaryKey: "CFBundleVersion") as? String
    
    print("Версия: \(version ?? "неизвестно")")
    print("Сборка: \(build ?? "неизвестно")")
}

// Проверка доступности функций
func checkFeatureAvailability() {
    if #available(iOS 15.0, *) {
        enableNewFeatures()
    } else {
        enableLegacyFeatures()
    }
}
