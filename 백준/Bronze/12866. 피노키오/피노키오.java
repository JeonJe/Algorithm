import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws Exception {
        int n = Integer.parseInt(br.readLine());
        char[] charArray = br.readLine().toCharArray();
        long[] counts = new long[4];

        for (char c : charArray) {
            if(c == 'A') {
                counts[0]++;
            } else if(c == 'C') {
                counts[1]++;
            } else if (c == 'G') {
                counts[2]++;
            } else if (c == 'T') {
                counts[3]++;
            }
        }
        if(counts[0] == 0 || counts[1] == 0 || counts[2] == 0 || counts[3] == 0) {
            System.out.println(0);
            return;
        }

        long answer = 1L;
        for (long count : counts) {
            answer = (answer * count) % 1_000_000_007;
        }
        
        System.out.println(answer);

    }

    private static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }


}