import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[][] board = new int[n][n];
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                board[i][j] = sc.nextInt();
            }
        }
        int result = 1;

        for(int i = 0; i < n; i++) {
            int prev = board[i][0];
            int continueCount = 1;
            for(int j = 1; j < n; j++) {
                int current = board[i][j];
                if(prev == current) {
                    continueCount++;
                } else {
                    continueCount = 1;
                }
                prev =current;
                if(continueCount >= m) {
                    result++;
                    break;
                }


            }
        }


        for(int i = 0; i < n; i++) {
            int prev = board[0][i];
            int continueCount = 1;
            for(int j = 1; j < n; j++) {
                int current = board[j][i];
                if(prev == current) {
                    continueCount++;
                } else {
                    continueCount = 1;
                }
                prev =current;
                if(continueCount >= m) {
                    result++;
                    break;
                }
            }
        }
        System.out.println(result);

    }

}