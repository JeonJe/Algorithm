
import java.util.Scanner;

class Main {
    public static int n;
    public static int m;
    public static int maxCellCount;
    public static int[][] board;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        board = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                board[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] > 0) {
                    calculate(i, j);
                }
            }
        }
        if(maxCellCount == 0) {
            System.out.println(-1);
        } else {
            System.out.println(maxCellCount);
        }
    }

    private static void calculate(int x, int y) {

        for (int i = x; i < n; i++) {
            for (int j = y; j < m; j++) {
                if (isAllPositive(x, i, y, j)) {
                    maxCellCount = Math.max(maxCellCount, (i - x + 1) * (j - y + 1));
                } else {
                    break;
                }
            }
        }

        for (int j = y; j < m; j++) {
            for (int i = x; i < n; i++) {
                if (isAllPositive(x, i, y, j)) {
                    maxCellCount = Math.max(maxCellCount, (i - x + 1) * (j - y + 1));
                } else {
                    break;
                }
            }
        }
    }


    private static boolean isAllPositive(int rowStart, int rowEnd, int colStart, int colEnd) {
        for (int i = rowStart; i <= rowEnd; i++) {
            for (int j = colStart; j <= colEnd; j++) {
                if (board[i][j] <= 0) {
                    return false;
                }
            }
        }
        return true;
    }
}



