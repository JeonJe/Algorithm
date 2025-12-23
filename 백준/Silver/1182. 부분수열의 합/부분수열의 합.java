import java.util.*;
import java.io.*;

public class Main {

    private static int answer = 0;
    private static int target = 0;
    private static int[] nums;
    private static int n = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        target = Integer.parseInt(st.nextToken());

        nums = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n; i++) {
            dfs(i, nums[i]);

        }
        System.out.println(answer);

    }

    private static void dfs(int start, int sum) {
        if (sum == target) {
            answer++;
        }

        for (int i = start + 1; i < nums.length; i++) {
            dfs(i, sum + nums[i]);
        }
    }


}
