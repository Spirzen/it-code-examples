
import Foundation

func scan(directory: URL, extension ext: String) -> (count: Int, bytes: Int64) {
    let fm = FileManager.default
    guard let enumerator = fm.enumerator(at: directory, includingPropertiesForKeys: [.fileSizeKey]) else {
        return (0, 0)
    }
    var count = 0, bytes: Int64 = 0
    for case let fileURL as URL in enumerator {
        guard fileURL.pathExtension == ext else { continue }
        count += 1
        if let size = try? fileURL.resourceValues(forKeys: [.fileSizeKey]).fileSize {
            bytes += Int64(size)
        }
    }
    return (count, bytes)
}
