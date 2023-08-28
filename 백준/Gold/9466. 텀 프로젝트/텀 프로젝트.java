import java.util.*;
import java.io.*;

public class Main {
  static int cntMadeTeamStudent;

  public static void main(String[] args) throws Exception {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(reader.readLine());

    for (int tc = 0; tc < T; tc++) {

      int N = Integer.parseInt(reader.readLine());
      int[] pick = new int[N + 1];
      boolean[] visited = new boolean[N + 1];
      boolean[] finished = new boolean[N + 1];

      StringTokenizer st = new StringTokenizer(reader.readLine());

      for (int i = 1; i < N + 1; i++) {
        pick[i] = Integer.parseInt(st.nextToken());
      }

      cntMadeTeamStudent = 0;
      for (int i = 1; i < N + 1; i++) {
        if (!visited[i]) {
          DFS(i, pick, visited, finished);
        }
      }
      System.out.println(N - cntMadeTeamStudent);
    // end of test case
    }    
  }

  static void DFS(int cur, int[] pick, boolean[] visited, boolean[] finished) {
    visited[cur] = true;
    int currentStudentWant = pick[cur];

    if (!visited[currentStudentWant]) {
      DFS(currentStudentWant, pick, visited, finished);
    } else if (!finished[currentStudentWant]) {
        cntMadeTeamStudent++;
        int ptr = currentStudentWant;
        while (ptr != cur) {
          cntMadeTeamStudent++;
          ptr = pick[ptr];
        }
      }
      finished[cur] = true;
    }
    
}
