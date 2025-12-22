import java.util.*;
import java.io.*;

public class Main {

  private static int maxSum = 0;

  public static void main(String[] args) throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());

    int[] nums = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      nums[i] = Integer.parseInt(st.nextToken());
    }

    int numsLength = nums.length;

    for (int i = 0; i < numsLength - 2; i++) {
      for (int j = i + 1; j < numsLength - 1; j++) {
        for (int k = j + 1; k < numsLength; k++) {
          int sum = nums[i] + nums[j] + nums[k];
          if (sum <= m) {
            maxSum = Math.max(maxSum, sum);
          }
        }
      }
    }
    System.out.println(maxSum);
  }

}
