class ImageProcessor {
    let sourcePath: String
    let targetFormat: String
    
    lazy var image: NSImage = {
        print("Загрузка изображения из \(sourcePath)")
        return NSImage(contentsOfFile: sourcePath) ?? NSImage()
    }()
    
    lazy var filters: [ImageFilter] = {
        print("Создание набора фильтров")
        return [
            BlurFilter(radius: 2.0),
            ContrastFilter(level: 1.2),
            SharpenFilter(amount: 0.8)
        ]
    }()
    
    lazy var cacheDirectory: URL = {
        let path = FileManager.default.urls(
            for: .cachesDirectory,
            in: .userDomainMask
        ).first
        return path?.appendingPathComponent("image_processor") ?? URL(fileURLWithPath: "/tmp")
    }()
    
    init(sourcePath: String, targetFormat: String) {
        self.sourcePath = sourcePath
        self.targetFormat = targetFormat
        print("Процессор изображений создан")
    }
    
    func process() {
        // Свойства инициализируются только при первом обращении
        _ = image
        _ = filters
        _ = cacheDirectory
        print("Обработка завершена")
    }
}
