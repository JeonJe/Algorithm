import java.util.*;
import java.io.*;

public class Main {

  public static void main(String[] args) throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int n = Integer.parseInt(st.nextToken());
    int answer = Integer.MAX_VALUE;

    // 216 - (9+9+9) = 216 - 27 = 189 부터 생성자 확인하면 됨
    //그거보다 더 작은 수로는 타겟인 216을 만들 수 없음
    int lowerBound = n - 9 * Integer.toString(n).length();
    for (int i = lowerBound; i < n; i++) {
      int candidate = i + digitSum(i);
      if (candidate == n) {
        answer = Math.min(answer, i);
        System.out.println(answer);
        return;

      }
    }
    System.out.println(0);
  }

  private static int digitSum(int x) {
    int sum = 0;
    while (x > 0) {
      sum += x % 10; // 꼬다리
      x /= 10;
    }
    return sum;
  }

}
