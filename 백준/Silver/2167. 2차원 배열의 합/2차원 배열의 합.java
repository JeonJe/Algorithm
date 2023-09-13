import java.util.*;
import java.io.*;

public class Main {
  public static void main(String[] args) throws Exception {
    
    StringBuilder sb = new StringBuilder();
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(reader.readLine());
    int height = Integer.parseInt(st.nextToken());
    int width = Integer.parseInt(st.nextToken());
    int[][] board = new int[height][width];
    
    for (int i = 0; i < height; i++) {
      st = new StringTokenizer(reader.readLine());
      for (int j = 0; j < width; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    int k = Integer.parseInt(reader.readLine());

    for (int i = 0; i < k; i++) {
      st = new StringTokenizer(reader.readLine());
      int startX = Integer.parseInt(st.nextToken())-1;
      int startY = Integer.parseInt(st.nextToken())-1;
      int endX = Integer.parseInt(st.nextToken());
      int endY = Integer.parseInt(st.nextToken());
      
      int sumBoard = 0;
      for (int x = startX; x < endX; x++) {
        
        for (int y = startY; y < endY; y++) {
          sumBoard += board[x][y];
        }
        
      }
      sb.append(sumBoard);
      sb.append("\n");
    }
    System.out.println(sb.toString());
  }
}
