import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws Exception {
        int n = Integer.parseInt(br.readLine());


        for(int i=0;i<n;i++){
            String[] inputs = br.readLine().split(" ");
            int[] nums = Arrays.stream(inputs).mapToInt(Integer::parseInt).toArray();

            int max = 0;
            for(int x = 0; x < nums.length-1; x++) {
                for(int y = x+1; y < nums.length; y++) {
                    max = Math.max(max, gcd(nums[x], nums[y]));
                }
            }
            sb.append(max).append("\n");
        }
        System.out.println(sb);

    }

    private static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }


}