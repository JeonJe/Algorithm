import java.util.*;
import java.io.*;

public class Main {
  static int height;
  static int width;
  static int[] dx = { 1, 0, -1, 0 };
  static int[] dy = { 0, 1, 0, -1 };
  public static void main(String[] args) throws Exception {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    int t = Integer.parseInt(reader.readLine());

    for (int tc = 0; tc < t; tc++) {
      StringTokenizer st = new StringTokenizer(reader.readLine());
      width = Integer.parseInt(st.nextToken());
      height = Integer.parseInt(st.nextToken());

      char[][] board = new char[height][width];
      boolean[][] visited = new boolean[height][width];
      for (int i = 0; i < height; i++) {
        board[i] = reader.readLine().toCharArray();
      }

      Queue<int[]> human = new ArrayDeque<int[]>();
      Queue<int[]> fire = new ArrayDeque<int[]>();

      for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
          if (board[i][j] == '@') {
            visited[i][j] = true;
            human.add(new int[] { i, j, 1 });
            
          } else if (board[i][j] == '*') {
            fire.add(new int[] { i, j });
          }
        }
      }

      int res = bfs(board, human, fire, visited);
      System.out.println(res > 0 ? res : "IMPOSSIBLE");

      // test case
    }
  }

  static int bfs(char[][] board, Queue<int[]> human, Queue<int[]> fire, boolean[][] visited) {
    boolean isExit = false;
    int dist = 0;

    
    while(!human.isEmpty()) {
    int humanSize = human.size();
    for (int k = 0; k < humanSize; k++) {
      int[] points = human.poll();
      int cx = points[0];
      int cy = points[1];
      int cdist = points[2];

      if (board[cx][cy] == '*') {
        continue;
      }

      for (int i = 0; i < 4; i++) {
        int nx = cx + dx[i];
        int ny = cy + dy[i];

        if (nx < 0 || nx >= height || ny < 0 || ny >= width) {
          isExit = true;
          dist = cdist;
          break;
        }

        if (!visited[nx][ny] && board[nx][ny] == '.') {
          visited[nx][ny] = true;
          human.add(new int[] { nx, ny, cdist + 1 });
        }
      }
    }
        
    if (isExit) {
      return dist;
    }
    int fireSize = fire.size();
    for( int k = 0 ; k < fireSize ; k++ ) {
      int[] firePoints = fire.poll();
      int fireCx = firePoints[0];
      int fireCy = firePoints[1];

      for (int i = 0; i < 4; i++) {
        int nextFireCx = fireCx + dx[i];
        int nextFireCy = fireCy + dy[i];

        if (0 <= nextFireCx && nextFireCx < height && 0 <= nextFireCy && nextFireCy < width) {
          if (board[nextFireCx][nextFireCy] == '.') {
            board[nextFireCx][nextFireCy] = '*';
            fire.add(new int[] { nextFireCx, nextFireCy });
          }
        }
      }
    }
  }
  
  return -1;
  }
}