import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
//        System.setIn(new FileInputStream("input.txt"));  // 제출 시 이 줄만 주석처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 1; i <= T; i++) {
            int target = Integer.parseInt(br.readLine());

            int result = dfs(1, target) + dfs(2, target) + dfs(3, target);
            System.out.println(result);
        }
    }

    //sum에서 Target까지 가는 방법의 수
    public static int dfs(int sum, int target) {
        if (sum > target) {
            return 0;
        }
        if (sum == target) {
            return 1;
        }

        //1을 선택했을 때 target까지 가는 방법의 수 + 2을 선택했을 때 target까지 가는 방법의 수 + 3을 선택했을 때 target까지 가는 방법의 수
        return dfs(sum + 1, target) + dfs(sum + 2, target) + dfs(sum + 3, target);
    }
}
