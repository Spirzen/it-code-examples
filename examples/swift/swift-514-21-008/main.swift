func application(_ application: UIApplication, 
                didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    application.setMinimumBackgroundFetchInterval(UIApplication.backgroundFetchIntervalMinimum)
    return true
}

func application(_ application: UIApplication, 
                performFetchWithCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    fetchData { result in
        switch result {
        case .success:
            completionHandler(.newData)
        case .noData:
            completionHandler(.noData)
        case .failed:
            completionHandler(.failed)
        }
    }
}
