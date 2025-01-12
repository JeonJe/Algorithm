
import java.util.Scanner;

class Main {

    public static int n;
    public static int m;
    public static int q;
    public static int[][] board;

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();
        board = new int[n][m];

        q = scanner.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                board[i][j] = scanner.nextInt();
            }
        }


        for (int t = 0; t < q; t++) {
            int targetRow = scanner.nextInt() - 1;
            String shiftDirection = scanner.next();
            boolean isShiftToLeft = shiftDirection.equals("R");
            shiftRow(targetRow, isShiftToLeft);
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }

    }

    private static void shiftRow(int targetRow, boolean isShiftToLeft) {
        shift(targetRow, isShiftToLeft);

        int currentUpsideRow = targetRow;
        int currentDownsideRow = targetRow;
        boolean upsideShiftDirection = isShiftToLeft;
        boolean downsideShiftDirection = isShiftToLeft;

        while (isMovable(currentUpsideRow, true)) {
            currentUpsideRow--;
            upsideShiftDirection = !upsideShiftDirection;
            shift(currentUpsideRow, upsideShiftDirection);
        }

        while (isMovable(currentDownsideRow, false)) {
            currentDownsideRow++;
            downsideShiftDirection = !downsideShiftDirection;
            shift(currentDownsideRow, downsideShiftDirection);
        }

    }

    public static boolean isMovable(int targetRow, boolean isUpside) {

        if (isUpside) {
            if (targetRow - 1 < 0) {
                return false;
            }
            return isSameNum(targetRow, targetRow - 1);
        }
        if (targetRow + 1 >= n) {
            return false;

        }
        return isSameNum(targetRow, targetRow + 1);

    }

    private static boolean isSameNum(int baseRow, int targetRow) {
        for (int i = 0; i < m; i++) {
            if (board[baseRow][i] == board[targetRow][i]) {
                return true;
            }
        }
        return false;
    }

    public static void shift(int targetRow, boolean isSfhitToLeft) {
        int temp;
        if (isSfhitToLeft) {
            temp = board[targetRow][0];
            for (int i = 0; i < m - 1; i++) {
                board[targetRow][i] = board[targetRow][i + 1];
            }
            board[targetRow][m - 1] = temp;
            return;
        }

        temp = board[targetRow][m - 1];
        for (int i = m - 1; i > 0; i--) {
            board[targetRow][i] = board[targetRow][i - 1];
        }
        board[targetRow][0] = temp;
    }

}

