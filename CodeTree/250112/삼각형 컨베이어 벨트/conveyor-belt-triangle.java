
import java.util.Scanner;

class Main {
    public static int n;
    public static int t;
    public static int[][] conveyBelt;
    public static int leftBottomCorner;
    public static int rightTopCorner;
    public static int rightMiddleCorner;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        t = sc.nextInt();

        conveyBelt = new int[3][n];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < n; j++) {
                conveyBelt[i][j] = sc.nextInt();
            }

        }

        for (int i = n - 1; i >= 0; i--) {
            conveyBelt[2][i] = sc.nextInt();
        }

        for (int i = 0; i < t; i++) {
            moveConveyBelt();
        }

        printConvey();

    }

    private static void printConvey() {
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(conveyBelt[i][j] + " ");
            }
            System.out.println();
        }
        for (int j = n - 1; j >= 0; j--) {
            System.out.print(conveyBelt[2][j] + " ");
        }
    }

    public static void moveConveyBelt() {
        moveTop();
        moveMiddle();
        moveBttom();
        conveyBelt[0][0] = leftBottomCorner;
        conveyBelt[1][0] = rightTopCorner;
        conveyBelt[2][n - 1] = rightMiddleCorner;

    }

    public static void moveTop() {
        rightTopCorner = conveyBelt[0][n - 1];
        for (int i = n - 1; i >= 1; i--) {
            conveyBelt[0][i] = conveyBelt[0][i - 1];
        }
    }

    public static void moveMiddle() {
        rightMiddleCorner = conveyBelt[1][n - 1];
        for (int i = n - 1; i >= 1; i--) {
            conveyBelt[1][i] = conveyBelt[1][i - 1];
        }
    }

    public static void moveBttom() {
        leftBottomCorner = conveyBelt[2][0];
        for (int i = 0; i < n - 1; i++) {
            conveyBelt[2][i] = conveyBelt[2][i + 1];
        }
    }
}



