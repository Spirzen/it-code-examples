
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        
        System.out.print("Введите имя: ");
        String name = reader.readLine();  // аналог input()
        
        System.out.print("Введите возраст: ");
        int age = Integer.parseInt(reader.readLine());  // как int(input())
        
        System.out.print("Введите рост: ");
        double height = Double.parseDouble(reader.readLine());  // как float(input())
        
        reader.close();
    }
}
