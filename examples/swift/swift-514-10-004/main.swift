let package = Package(
    name: "MyLibrary",
    platforms: [.iOS(.v15), .macOS(.v12)],
    products: [
        .library(name: "MyLibrary", targets: ["MyLibrary"])
    ],
    dependencies: [
        .package(url: "https://github.com/Alamofire/Alamofire.git", from: "5.8.0")
    ],
    targets: [
        .target(name: "MyLibrary", dependencies: ["Alamofire"]),
        .testTarget(name: "MyLibraryTests", dependencies: ["MyLibrary"])
    ]
)
