import java.util.*;

public class Main {
    private static int[][] board;
    private static int n;
    private static int m;

    private static int blockA(int i, int j) {
        int max = 0;
        if(i + 1 < n && j + 1 < m) {
            max = Math.max(max, board[i][j] + board[i + 1][j] + board[i][j+1]);
        }
        if(i+1 < n && j -1 >= 0) {
            max = Math.max(max, board[i][j] + board[i+1][j] + board[i][j-1]);
        }
        if(i-1 >= 0 && j + 1 < m) {
            max = Math.max(max, board[i][j] + board[i-1][j] + board[i][j+1]);
        }
        if(i-1 >= 0 && j - 1 >= 0) {
            max = Math.max(max, board[i][j] + board[i-1][j] + board[i][j-1]);
        }
        return max;
    }

    private static int blockB(int i, int j) {
        int max = 0;
        if(i + 2 < n) {
            max = Math.max(max, board[i][j] + board[i + 1][j] + board[i + 2][j]);
        }
        if(i - 2 >= 0) {
            max = Math.max(max, board[i][j] + board[i - 1][j] + board[i - 2][j]);
        }
        if(j + 2 < m) {
            max = Math.max(max, board[i][j] + board[i][j + 1] + board[i][j + 2]);
        }
        if(j - 2 >= 0) {
            max = Math.max(max, board[i][j] + board[i][j - 1] + board[i][j - 2]);
        }
        return max;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

       board = new int[n][m];
        for (int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                board[i][j] = sc.nextInt();
            }
        }
        int result = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                result =  Math.max(blockA(i, j), result);
               result =  Math.max(blockB(i, j), result);
            }
        }
        System.out.println(result);

    }



}