import java.util.*;
import java.io.*;

public class BOJ_14502 {
  static StringTokenizer st;
  static int[][] board;
  static List<int[]> virus = new ArrayList<int[]>();
  static List<int[]> emptyArea = new ArrayList<int[]> ();
  static int height, width;
  static int[] dx = {1,0,-1,0}, dy = {0,1,0,-1};
  public static void main(String[] args) throws Exception {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    st = new StringTokenizer(reader.readLine());
    height = Integer.parseInt(st.nextToken());
    width = Integer.parseInt(st.nextToken());
    board = new int[height][width];

    for(int i = 0 ; i < height; i++ ) {
      st = new StringTokenizer(reader.readLine());
      for (int j = 0; j < width; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
        if( board[i][j] == 0) {
          emptyArea.add(new int[]{i, j});
        } else if ( board[i][j] == 2 ) {
          virus.add(new int[]{i, j});
        }
      }
    }
    int answer = 0;
    for (int i = 0; i < emptyArea.size()-2; i++) {
      for (int j = i+1; j < emptyArea.size()-1; j++) {
        for (int k = j+1; k < emptyArea.size(); k++) {
          board[emptyArea.get(i)[0]][emptyArea.get(i)[1]] = 1;
          board[emptyArea.get(j)[0]][emptyArea.get(j)[1]] = 1;
          board[emptyArea.get(k)[0]][emptyArea.get(k)[1]] = 1;
          answer = Math.max(answer,findSafeArea());
          board[emptyArea.get(i)[0]][emptyArea.get(i)[1]] = 0;
          board[emptyArea.get(j)[0]][emptyArea.get(j)[1]] = 0;
          board[emptyArea.get(k)[0]][emptyArea.get(k)[1]] = 0;
        }
      }
    }
    System.out.println(answer);

  }  

  static int findSafeArea(){
    int area = 0;
    boolean[][] visited = new boolean[height][width];

    for (int i = 0; i < virus.size(); i++) {
      int x = virus.get(i)[0], y = virus.get(i)[1];
      visited[x][y] = true;
      dfs(x,y,visited);
    }

    for (int i = 0; i < height; i++) {
      for (int j = 0; j < width; j++) {
        if (board[i][j] == 0 && !visited[i][j]) {
          area++;
        }
      }
    }
    return area;
  }

  static void dfs(int x, int y, boolean[][] visited) {
    
    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];

      if (0 <= nx && nx < height && 0 <= ny && ny < width) {
        if(board[nx][ny] == 0 && !visited[nx][ny]) {
          visited[nx][ny] = true;
          dfs(nx,ny,visited);
        }
      }
    }
  }

}
