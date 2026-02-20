import java.util.*;
import java.io.*;

public class BOJ_1389 {
  static int N, M;
  public static void main(String[] args) throws Exception {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(reader.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    int[][] distance = new int[N+1][N+1];
    for (int i = 0; i < N+1; i++) {
      for (int j = 0; j < N+1; j++) {
        if (i != j) {
          distance[i][j] = 5001;
        }
      }
    }

    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(reader.readLine());
      int fr = Integer.parseInt(st.nextToken());
      int to = Integer.parseInt(st.nextToken());
      distance[fr][to] = 1;
      distance[to][fr] = 1;
    }

    for (int k = 1; k < N+1; k++) {
      for (int i = 1; i < N+1; i++) {
        for (int j = 1; j < N+1; j++) {
          distance[i][j] = Math.min(distance[i][j], distance[i][k] + distance[k][j]);
        }
      }
    }

    int cntRelation = 5001;
    int userNumber = 5001;

    for (int i = N; i > 0; i--) {
      int relation = 0;
      for (int j = 1; j < N+1; j++) {
        relation += distance[i][j];
      }
      if (relation <= cntRelation) {
        cntRelation = relation;
        userNumber = i;
      }
    }
    System.out.println(userNumber);
  }
  
}
