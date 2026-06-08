
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class HashExample {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        String text = "Привет, мир!";
        System.out.println("Исходный текст: " + text);
        
        // Хеширование SHA-256
        MessageDigest sha256 = MessageDigest.getInstance("SHA-256");
        byte[] hashBytes = sha256.digest(text.getBytes());
        String sha256Hash = bytesToHex(hashBytes);
        System.out.println("SHA-256: " + sha256Hash);
        
        // Хеширование MD5
        MessageDigest md5 = MessageDigest.getInstance("MD5");
        byte[] md5Bytes = md5.digest(text.getBytes());
        String md5Hash = bytesToHex(md5Bytes);
        System.out.println("MD5: " + md5Hash);
    }
    
    private static String bytesToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }
}
