import java.util.*;
import java.io.*;

public class Main {
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
    boolean[] visited = new boolean[F+1];
    visited[S] = true;
    Queue<int[]> queue = new ArrayDeque<int[]>();
    queue.add(new int[]{S, 0});

    while(!queue.isEmpty()) {
      int[] current = queue.poll();
      int currentPoint = current[0];
      int dist = current[1];

      if (currentPoint == G) {
        return dist;
      }
      if (currentPoint + U <= F && !visited[currentPoint + U]) {
        visited[currentPoint + U] = true;
        queue.add(new int[]{currentPoint + U, dist+1});  
      } 
      if (currentPoint - D >= 1 && !visited[currentPoint - D]) {
        visited[currentPoint - D] = true;
        queue.add(new int[]{currentPoint - D, dist+1});
      }
      
    }

    return -1;

  }
}
