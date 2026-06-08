
import java.io.IOException;
import java.io.FileNotFoundException;

class DataProcessor {
    public void process() throws IOException {
        System.out.println("Processing data...");
    }
}

class ImageProcessor extends DataProcessor {
    @Override
    public void process() throws FileNotFoundException { // подтип IOException
        System.out.println("Processing image...");
    }
}
