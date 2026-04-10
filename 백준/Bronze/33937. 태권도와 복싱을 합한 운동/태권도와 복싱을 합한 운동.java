import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int n = 0, m = 0;
    static boolean[] visited;

    static List<Character> vowels = List.of('a', 'e', 'i', 'o', 'u');
    public static void main(String[] args) throws Exception {
        String a = br.readLine();
        String b = br.readLine();


        String checkA = check(a);
        String checkB = check(b);

        if (checkA.isEmpty() || checkB.isEmpty()) {
            System.out.println("no such exercise");
            return;
        }

        System.out.println(checkA + checkB);


    }

    //문자열의 첫음절이란 문자열의 첫 번째 모음을 포함하고 그다음 나오는 첫 번째 자음을 포함하지 않는 접두사 중 가장 긴 접두사이다.
    // 만약 모음이 없거나 첫 번째 모음 이후 자음이 없다면 첫음절은 존재하지 않는다.
    private static String check(String str) {

        //첫 번째  모음 위치
        int firstVowel = -1;
        char[] charArray = str.toCharArray();
        
        for (int i = 0; i < str.length(); i++) {
            vowels.indexOf(charArray[i]);
            if (vowels.contains(charArray[i])) {
                firstVowel = i;
                break;
            }
        }

        // 첫번째 모음 위치 이후 첫번째 자음 위치
        int firstConsonant = -1;
        for (int i = firstVowel + 1; i < str.length(); i++) {
            if (!vowels.contains(charArray[i])) {
                firstConsonant = i;
                break;
            }
        }

        if(firstVowel == -1 || firstConsonant == -1) return "";

        return str.substring(0, firstConsonant);

    }
}