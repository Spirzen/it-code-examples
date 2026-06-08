public class YoungGenExample {
    public static void main(String[] args) {
        // Объекты создаются в Eden
        byte[] data1 = new byte[1024 * 100]; // 100 KB
        byte[] data2 = new byte[1024 * 200]; // 200 KB
        
        // После нескольких циклов сборки мусора
        // выжившие объекты перемещаются в Survivor
        
        for (int i = 0; i < 1000; i++) {
            byte[] temp = new byte[1024 * 50];
            // временные объекты быстро удаляются из Eden
        }
        
        // Объекты, пережившие несколько сборок,
        // перемещаются в Old Generation
        byte[] longLived = new byte[1024 * 1024 * 10]; // 10 MB
        keepReference(longLived);
    }
    
    static void keepReference(byte[] data) {
        // объект остаётся достижимым
    }
}
