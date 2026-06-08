// Адаптер: делаем старый API совместимым с новым
public class LegacyFileReader { public string ReadOldFormat() { ... } }
public class FileReaderAdapter : IFileReader { 
    private readonly LegacyFileReader _legacy;
    public string Read() => _legacy.ReadOldFormat().Replace(";", ","); 
}

// Фасад: упрощаем работу с архивом + шифрованием + логированием
public class SecureArchiveFacade {
    public string ReadFile(string path) {
        var archive = new ArchiveExtractor();
        var crypto = new Decryptor();
        var logger = new AuditLogger();
        logger.Log("Extracting...");
        var data = archive.Extract(path);
        logger.Log("Decrypting...");
        return crypto.Decrypt(Данные);
    }
}

// Proxy: ленивая загрузка + кэширование
public class LazyFileProxy : IFileReader {
    private IFileReader _realReader;
    private string _cache;
    public string Read() {
        if (_cache == null) {
            _realReader ??= new RealFileReader();
            _cache = _realReader.Read();
        }
        return _cache;
    }
}
