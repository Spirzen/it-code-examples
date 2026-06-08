
import java.io.IOException;

class FileReader {
    public void read() throws IOException {
        System.out.println("Reading file...");
    }
}

class SecureFileReader extends FileReader {
    // ❌ ОШИБКА КОМПИЛЯЦИИ
    @Override
    public void read() throws Exception { // Exception шире IOException
        System.out.println("Secure reading...");
    }
}
