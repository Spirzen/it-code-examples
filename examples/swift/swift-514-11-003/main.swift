// swift-tools-version:5.9

import PackageDescription

let package = Package(
  name: "MyLibrary",
  platforms: [.iOS(.v15), .macOS(.v12)],
  products: [
    .library(name: "Core", targets: ["Core"]),
  ],
  dependencies: [
    .package(url: "https://github.com/apple/swift-algorithms", from: "1.0.0"),
  ],
  targets: [
    .target(name: "Core", dependencies: ["Algorithms"]),
    .testTarget(name: "CoreTests", dependencies: ["Core"]),
  ]
)
