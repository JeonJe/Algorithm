import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());
        int result = 0;

        for (int testCase = 0; testCase < t; testCase++) {
            String word = reader.readLine();
            if(groupChecker(word)) {
                result++;
            }

        }
        System.out.println(result);
    }

        private static boolean groupChecker(String word) {
        Set<Character> seenCharacters = new HashSet<>();
        char prevChar = word.charAt(0);
        seenCharacters.add(prevChar);

        for (int i = 1; i < word.length(); i++) {
            char currentChar = word.charAt(i);
            
            if (currentChar != prevChar && seenCharacters.contains(currentChar)) {
                return false;
            }
            seenCharacters.add(currentChar);
            prevChar = currentChar; 
        }
        return true;
    }
}