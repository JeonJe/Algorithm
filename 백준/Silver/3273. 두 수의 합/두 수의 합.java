import java.io.BufferedReader;
//import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int target;
    private static int result;
    private static int[] nums;

    public static void main(String[] args) throws Exception {
//        System.setIn(new FileInputStream("input.txt"));  // 제출 시 이 줄만 주석처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        nums = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        target = Integer.parseInt(br.readLine());

        Arrays.sort(nums);

        int left = 0;
        int right = n - 1;

        while (left < right) {
            int sum = nums[left] + nums[right];
            if (sum == target) {
                result++;
                left++;
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
         System.out.println(result);
    }

}
