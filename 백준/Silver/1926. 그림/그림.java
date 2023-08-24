import java.util.*;
import java.io.*;

public class Main {
  static int n;
  static int m;
  static int[][] board;
  static boolean[][] visited;
  static int[] dx = {1,0,-1,0};
  static int[] dy = {0,1,0,-1};
  public static void main(String[] args) throws Exception {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(rd.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    board = new int[n][m];
    visited = new boolean[n][m];

    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(rd.readLine());
      for (int j = 0; j < m; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }
    int cntPictures = 0;
    int maxArea = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (!visited[i][j] && board[i][j] == 1) {
          cntPictures++;
          int result = bfs(i,j);
          maxArea = Math.max(maxArea, result);
        }
      }
    }
    System.out.println(cntPictures);
    System.out.println(maxArea);
  }
  static int bfs(int x, int y) {
    visited[x][y] = true;
    Queue<int[]> deque = new ArrayDeque<int[]>() ;
    deque.add(new int[]{x, y});
    int cntDist = 1;
    
    while(!deque.isEmpty()) {
      int[] current = deque.poll();
      int cx = current[0];
      int cy = current[1];

      for (int i = 0; i < 4; i++) {
        int nx = cx + dx[i];
        int ny = cy + dy[i];

        if ( 0 <= nx && nx < n && 0 <= ny && ny < m ) {
          if (!visited[nx][ny] && board[nx][ny] == 1) {
            visited[nx][ny] = true;
            cntDist++;
            deque.add(new int[]{nx, ny});
          }
        }
      }
    }

    return cntDist;
  }
}
