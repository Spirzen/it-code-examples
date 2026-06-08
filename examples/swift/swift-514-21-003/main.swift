func applicationWillFinishLaunchingWithOptions(_ launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // Инициализация до полного запуска
    setupCoreServices()
    return true
}

func application(_ application: UIApplication, 
                didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // Завершение настройки после запуска
    configureAppearance()
    setupNavigation()
    return true
}

func applicationDidBecomeActive(_ application: UIApplication) {
    // Приложение готово к взаимодействию
    resumeTasks()
    refreshData()
}
