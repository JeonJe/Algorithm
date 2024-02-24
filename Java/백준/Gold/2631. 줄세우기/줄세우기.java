import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        int[] dp = new int[N];

        for (int i = 0 ; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        for (int i = 0; i < N; i++) {
            int IS = 0;
            for (int j = i-1; j >=0; j--){
                if(arr[j] < arr[i]){
                    IS = Math.max(IS, dp[j]);
                }
            }
            dp[i] = IS+1;
        }

        System.out.println(N - Arrays.stream(dp).max().getAsInt());

    }
}
