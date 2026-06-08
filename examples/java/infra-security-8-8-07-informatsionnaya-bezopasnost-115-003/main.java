
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.util.Base64;

public class AesExample {
    public static void main(String[] args) throws Exception {
        // Генерация ключа
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(256);
        SecretKey secretKey = keyGen.generateKey();
        
        // Исходный текст
        String plaintext = "Secret message";
        System.out.println("Открытый текст: " + plaintext);
        
        // Шифрование
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes());
        
        System.out.println("Шифротекст (Base64): " + Base64.getEncoder().encodeToString(ciphertext));
    }
}
