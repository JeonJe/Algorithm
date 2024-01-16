import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            List<List<Character>> charList = new ArrayList<>();
            String line;

            while((line = br.readLine()) != null && !line.isEmpty()) {
                List<Character> row = new ArrayList<>();

                for (int i = 0; i < 15; i++){
                    if (i >= line.toCharArray().length) {
                        row.add('_');
                    } else {
                        row.add(line.toCharArray()[i]);
                    }

                }
                charList.add(row);
            }
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < 15; i++) {
                for (int j = 0; j < 5; j++) {
                    result.append(charList.get(j).get(i));
                }
            }
            System.out.println(result.toString().replaceAll("_", ""));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}