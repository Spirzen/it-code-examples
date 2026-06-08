import java.util.*;

public class WordFrequency {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Map<String, Integer> freq = new HashMap<>();
        while (sc.hasNext()) {
            String word = sc.nexttoLowerCase();
            freq.merge(word, 1, Integer::sum);
        }
        for (Map.Entry<String, Integer> e : freq.entrySet()) {
            System.out.println(e.getKey() + ": " + e.getValue());
        }
        sc.close();
    }
}
