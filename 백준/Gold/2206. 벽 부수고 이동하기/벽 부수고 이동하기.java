import java.util.*;
import java.io.*;

public class Main {
  static int height;
  static int width;
  static int[][] board;
  static int[] dx = {1,0,-1,0};
  static int[] dy = {0,1,0,-1};
  static int[][][] visited;
  static int answer = 0;
  public static void main(String[] args) throws Exception {

    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(reader.readLine());
    height = Integer.parseInt(st.nextToken());
    width = Integer.parseInt(st.nextToken());
    board = new int[height][width];
    visited = new int[height][width][2];

    for (int i = 0 ; i < height; i++) {
      char[] currentLine = reader.readLine().toCharArray();
      for (int j = 0; j < width; j++) {
        board[i][j] = Character.getNumericValue(currentLine[j]);
      }
    }

    BFS(0,0);
    System.out.println(answer);
  }

  static void BFS(int x, int y) {
    Queue<int[]> queue = new ArrayDeque<int[]>();
    queue.add(new int[]{x, y, 1});

    while (!queue.isEmpty()) {
      int[] currentInfo = queue.poll();
      int cx = currentInfo[0];
      int cy = currentInfo[1];
      int chance = currentInfo[2];
      
      if (cx == height-1 && cy == width - 1) {
        answer = visited[cx][cy][chance]+1;
        return ;
      }

      for (int i = 0; i < 4; i++) {
        int nx = cx + dx[i];
        int ny = cy + dy[i];

        if( 0 <= nx && nx < height && 0 <= ny && ny < width && visited[nx][ny][chance] == 0) {
          //벽을 부순적이 없고 다음 좌표가 빈 공간
          if (chance == 1 && board[nx][ny] == 0) {
            visited[nx][ny][chance] = visited[cx][cy][chance] + 1;
            queue.add(new int[]{nx, ny, chance});
          }
          //벽을 부순적이 없고 다음 좌표가 벽
          else if (chance == 1 && board[nx][ny] == 1) {
            visited[nx][ny][0] = visited[cx][cy][chance] + 1;
            queue.add(new int[]{nx, ny, 0});
          }

          //벽을 부순적이 있고 다음좌표가 방문할 수 있는 빈칸 
          else if (chance == 0 && board[nx][ny] == 0) {
            visited[nx][ny][chance] = visited[cx][cy][chance] + 1;
            queue.add(new int[]{nx, ny, chance});
          }
        }
      }
      
    }
    answer = -1;
  }
}