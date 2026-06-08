class AppDelegate: UIResponder, UIApplicationDelegate {
    
    var window: UIWindow?
    
    func application(_ application: UIApplication, 
                    willFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        print("Приложение начинает запуск")
        return true
    }
    
    func applicationDidBecomeActive(_ application: UIApplication) {
        print("Приложение стало активным")
    }
    
    func applicationWillResignActive(_ application: UIApplication) {
        print("Приложение покидает активное состояние")
    }
    
    func applicationDidEnterBackground(_ application: UIApplication) {
        print("Приложение перешло в фоновый режим")
    }
    
    func applicationWillEnterForeground(_ application: UIApplication) {
        print("Приложение возвращается из фонового режима")
    }
    
    func applicationWillTerminate(_ application: UIApplication) {
        print("Приложение завершает работу")
    }
}
