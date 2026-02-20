
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] board = new int[n][n];

        for(int i = 0; i < n; i++) {
            for(int j =0; j < n; j++) {
                board[i][j] = sc.nextInt();
            }
        }

        int result = 0;
        for(int i = 0; i < n-2; i++) {
            for(int j = 0; j < n-2; j++) {
                int sum = 0;
                for(int dx =0; dx < 3; dx++) {
                    for(int dy =0; dy < 3; dy++) {
                        sum += board[i+dx][j+dy];
                    }
                }
                result = Math.max(result, sum);
            }

        }
        System.out.println(result);

    }

}