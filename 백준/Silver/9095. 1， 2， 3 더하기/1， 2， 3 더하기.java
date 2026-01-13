import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int count = 0;

    public static void main(String[] args) throws Exception {
//        System.setIn(new FileInputStream("input.txt"));  // 제출 시 이 줄만 주석처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 1; i <= T; i++) {
            int target = Integer.parseInt(br.readLine());

            count = 0;
            dfs(1, target);
            dfs(2, target);
            dfs(3, target);
            System.out.println(count);
        }
    }

    public static void dfs(int sum, int target) {
        if (sum > target) {
            return;
        }
        if (sum == target) {
            count++;
            return;
        }

        dfs(sum + 1, target);
        dfs(sum + 2, target);
        dfs(sum + 3, target);
    }
}
