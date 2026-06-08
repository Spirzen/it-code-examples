func parseVersion(_ raw: String) -> (major: Int, minor: Int)? {
    let parts = raw.split(separator: ".")
    guard parts.count == 2,
          let major = Int(parts[0]),
          let minor = Int(parts[1]) else {
        return nil
    }
    return (major: major, minor: minor)
}

if let version = parseVersion("5.9") {
    print(version.major)   // 5
    print(version.minor)   // 9
}
