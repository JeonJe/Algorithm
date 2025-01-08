
import java.util.*;

public class Main {
    private static int[][] board;
    private static int n;
    private static int m;

    private static int[] dx = {0,1,1,1,0,-1,-1,-1};
    private static int[] dy = {-1,-1,0,1,1,1,0,-1};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

       board = new int[n][n];
        for (int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                board[i][j] = sc.nextInt();
            }
        }

        int gainGoldCount = 0;
        for (int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                for(int k = 0; k <= n; k++) {
                    gainGoldCount = Math.max(gainGoldCount, mining(i, j, k));
                }
            }
        }

        System.out.println(gainGoldCount);
    }

    private static int mining(int x, int y, int k) {
        int cellCount = 0;
        int goldCount = 0;

        for (int dx = -k; dx <= k; dx++) {
            for (int dy = -(k - Math.abs(dx)); dy <= (k - Math.abs(dx)); dy++) {
                if (isValid(x + dx, y + dy)) {
                    if (board[x + dx][y + dy] == 1) {
                        goldCount++;
                    }
                }
            }
        }

        int working = (k * k) + (k + 1) * ( k+ 1);
        int gaining = goldCount * m;

        return gaining >= working ? goldCount : 0;
    }

    private static boolean isValid(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < n;
    }


}