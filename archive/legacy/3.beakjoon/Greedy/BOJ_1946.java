import java.util.*;
import java.io.*;

public class BOJ_1946 {
  public static void main(String[] args) throws Exception {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(reader.readLine());

    for (int i = 0; i < T; i++) {
      int N = Integer.parseInt(reader.readLine());

      // 2차원 배열
      int[][] seq = new int[N][2];

      for (int j = 0; j < N; j++) {
        StringTokenizer st = new StringTokenizer(reader.readLine());
        int k = 0;
        while (st.hasMoreTokens()) {
          seq[j][k] = Integer.parseInt(st.nextToken());
          k++;
        }
      }
      Arrays.sort(seq, (o1, o2) -> {
          return o1[0] - o2[0];
      });
      int answer = 1;
      int prev = seq[0][1];
      for (int j = 1; j < N; j++) {
        if (prev > seq[j][1]) {
          prev = seq[j][1];
          answer++;
        }
      }
    //test case 종료
      System.out.println(answer);
    }
  }
}
