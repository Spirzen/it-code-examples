class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    
    var window: UIWindow?
    
    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, 
              options connectionOptions: UIScene.ConnectionOptions) {
        guard let windowScene = scene as? UIWindowScene else { return }
        
        window = UIWindow(windowScene: windowScene)
        window?.rootViewController = ViewController()
        window?.makeKeyAndVisible()
    }
    
    func sceneDidDisconnect(_ scene: UIScene) {
        // Сцена отключена от сессии
    }
    
    func sceneDidBecomeActive(_ scene: UIScene) {
        // Сцена стала активной
    }
    
    func sceneWillResignActive(_ scene: UIScene) {
        // Сцена покидает активное состояние
    }
    
    func sceneDidEnterBackground(_ scene: UIScene) {
        // Сцена перешла в фоновый режим
    }
    
    func sceneWillEnterForeground(_ scene: UIScene) {
        // Сцена возвращается из фонового режима
    }
}
