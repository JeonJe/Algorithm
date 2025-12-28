import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());

        int[] nums = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nums);
        int left = 0;
        int right = n - 1;

        int count = 0;

        while (left < right) {

            if ((nums[left] + nums[right]) < m) {
                left++;
            } else if (nums[left] + nums[right] == m) {
                count++;
                left++;
                right--;
            } else {
                right--;
            }
        }
        System.out.println(count);
    }


}
