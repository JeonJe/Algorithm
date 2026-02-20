import java.util.*;
import java.io.*;

public class BOJ_5014 {
  static int F, S, G, U, D;

  public static void main(String[] args) throws Exception {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(reader.readLine());

    F = Integer.parseInt(st.nextToken());
    S = Integer.parseInt(st.nextToken());
    G = Integer.parseInt(st.nextToken());
    U = Integer.parseInt(st.nextToken());
    D = Integer.parseInt(st.nextToken());

    int res = bfs();
    System.out.println(res >= 0 ? res : "use the stairs");

  }

  static int bfs() {
    boolean[] visited = new boolean[F + 1];
    visited[S] = true;
    Queue<int[]> queue = new ArrayDeque<int[]>();
    queue.add(new int[] { S, 0 });
    int[] move = new int[] { U, -D };

    while (!queue.isEmpty()) {
      int[] current = queue.poll();
      int currentPoint = current[0];
      int dist = current[1];

      if (currentPoint == G) {
        return dist;
      }
      for (int i = 0; i < move.length; i++) {
        int next = currentPoint + move[i];
        if (1 <= next && next <= F && !visited[next]) {
          visited[next] = true;
          queue.add(new int[] { next, dist + 1 });
        }
      }
    }

    return -1;

  }
}
