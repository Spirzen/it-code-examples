public class FileProcessor {
    
    public void processLargeFile(Path filePath) throws IOException {
        try (BufferedReader reader = Files.newBufferedReader(filePath)) {
            String line;
            while ((line = reader.readLine()) != null) {
                processLine(line);
            }
        }
    }
    
    public void writeLargeFile(Path filePath, List<String> lines) throws IOException {
        try (BufferedWriter writer = Files.newBufferedWriter(filePath)) {
            for (String line : lines) {
                writer.write(line);
                writer.newLine();
            }
        }
    }
    
    public long countLines(Path filePath) throws IOException {
        try (Stream<String> lines = Files.lines(filePath)) {
            return lines.count();
        }
    }
}
