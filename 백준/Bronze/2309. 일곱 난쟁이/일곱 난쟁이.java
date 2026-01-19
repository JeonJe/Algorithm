import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.System.exit;

public class Main {

    private static int[] nums;
    private static int[] temp;

    public static void main(String[] args) throws Exception {
        //System.setIn(new FileInputStream("input.txt"));  // 제출 시 이 줄만 주석처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        nums = new int[9];
        temp = new int[7];
        for (int i = 0; i < 9; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }


        Arrays.sort(nums);

        temp[0] = 0;
        dfs(0, temp, 0, 0);

    }

    private static void dfs(int idx, int[] temp, int sum, int cnt) {
        if (cnt == 7) {
            if (sum == 100) {
                for (int i = 0; i < 7; i++) {
                    System.out.println(temp[i]);
                }
                exit(0);
            }
            return;
        }

        for (int i = idx; i < 9; i++) {
            temp[cnt] = nums[i];
            dfs(i + 1, temp, sum + nums[i], cnt + 1);
        }
    }
}
