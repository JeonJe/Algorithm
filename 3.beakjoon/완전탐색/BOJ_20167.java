import java.util.*;
import java.io.*;

public class BOJ_20167 {
  static int answer = 0;
  static int N, K = 0;
  static int[] seq;

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    K = Integer.parseInt(st.nextToken());

    int[] seq = new int[N];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) {
      seq[i] = Integer.parseInt(st.nextToken());
    }

    for (int i = 0; i < (1 << N); i++) {
      int satisfaction = 0;
      int energy = 0;

      for (int j = 0; j < N; j++) {
        if ((i & (1 << j)) > 0) {
          if (satisfaction + seq[j] >= K) {
            energy += satisfaction + seq[j] - K;
            satisfaction = 0;
          } else {
            satisfaction += seq[j];
          }

        } else {
          satisfaction = 0;
        }

        answer = Math.max(answer, energy);
      }
      System.out.println(answer);

    }

  }
}
