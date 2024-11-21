
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        while(true) {
            String input = reader.readLine();
            if (input == null || input.isEmpty()) break;

            StringTokenizer stringTokenizer = new StringTokenizer(input);
            int A = Integer.parseInt(stringTokenizer.nextToken());
            int B = Integer.parseInt(stringTokenizer.nextToken());
            System.out.println(A + B);
        }
    }

}
