func applicationWillResignActive(_ application: UIApplication) {
    // Подготовка к переходу в фон
    pauseMedia()
    saveTemporaryData()
}

func applicationDidEnterBackground(_ application: UIApplication) {
    // Приложение в фоновом режиме
    var task: UIBackgroundTaskIdentifier = .invalid
    task = application.beginBackgroundTask {
        application.endBackgroundTask(task)
        task = .invalid
    }
    performBackgroundTasks(task)
}
