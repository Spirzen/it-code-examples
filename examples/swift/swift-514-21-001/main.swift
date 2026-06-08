// Package.swift для Swift Package Manager
let package = Package(
    name: "MyApplication",
    platforms: [
        .iOS(.v15)
    ],
    products: [
        .library(
            name: "MyApplication",
            targets: ["MyApplication"]
        )
    ],
    dependencies: [],
    targets: [
        .target(
            name: "MyApplication",
            dependencies: []
        )
    ]
)
