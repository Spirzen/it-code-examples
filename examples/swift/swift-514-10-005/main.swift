let project = Project(
    name: "App",
    targets: [
        Target(
            name: "App",
            platform: .iOS,
            product: .app,
            bundleId: "ru.spirzen.App",
            infoPlist: "Info.plist",
            sources: ["Sources/**"],
            dependencies: [.sdk(name: "StoreKit.framework")]
        )
    ]
)
