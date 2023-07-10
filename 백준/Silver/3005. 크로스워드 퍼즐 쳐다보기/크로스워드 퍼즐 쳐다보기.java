import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int R = Integer.parseInt(st.nextToken());
    int C = Integer.parseInt(st.nextToken());

    char [][] board = new char[R][C];
    
    for (int i = 0; i < R; i++) {
      board[i] =  br.readLine().toCharArray();
    }
    Set<String> bucket = new HashSet<String>();

    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        if (board[i][j] != '#'){
          findWord(i,j,board, bucket);
        }
      }
    }

    List<String> sortedBucket = new ArrayList<>(bucket);
    Collections.sort(sortedBucket);

    System.out.println(sortedBucket.get(0));
    
  }

  private static void findWord(int x, int y, char[][] board, Set<String> bucket){
    Deque<Character> que = new ArrayDeque<>();

    que.add(board[x][y]);

    int ly = y - 1;
    while (ly >= 0 && board[x][ly] != '#'){
      que.addFirst(board[x][ly]);
      ly--;
    }

    int ry = y + 1;
    while (ry < board[0].length && board[x][ry] != '#'){
      que.add(board[x][ry]);
      ry++;
    }

    StringBuilder wordBuilder = new StringBuilder();
    for (char c : que) {
      wordBuilder.append(c);
    }
    String word = wordBuilder.toString();
    if (word.length() > 1){
      bucket.add(word);
    }

    que.clear();
    que.add(board[x][y]);

    int tx = x - 1;
    while (tx >= 0 && board[tx][y] != '#'){
      que.addFirst(board[tx][y]);
      tx--;
    }

    int bx = x + 1;
    while ( bx < board.length && board[bx][y] != '#'){
      que.add(board[bx][y]);
      bx++;
    }

    wordBuilder = new StringBuilder();
    for (char c : que){
      wordBuilder.append(c);
    }
    
    word = wordBuilder.toString();
    if (word.length() > 1){
      bucket.add(word);
    }
  }
  
}
