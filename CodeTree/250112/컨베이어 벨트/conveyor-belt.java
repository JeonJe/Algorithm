

import java.util.Scanner;

class Main {
    public static int n;
    public static int t;
    public static int[][] conveyBelt;
    public static int leftBottomCorner;
    public static int rightTopCorner;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        t = sc.nextInt();

        conveyBelt = new int[2][n];
        for (int j = 0; j < n ; j++) {
            conveyBelt[0][j] = sc.nextInt();
        }

        for (int j = n-1; j >= 0 ; j--) {
            conveyBelt[1][j] = sc.nextInt();
        }

        for(int i = 0; i < t; i++) {
            moveConveyBelt();
        }

        printConvey();

    }

    private static void printConvey() {
        for(int i = 0; i < n; i++) {
            System.out.print(conveyBelt[0][i] + " ");
        }
        System.out.println();
        for(int i = n-1; i >= 0 ; i--) {
            System.out.print(conveyBelt[1][i] + " ");
        }
    }

    public static void moveConveyBelt() {
        moveToRight();
        moveToLeft();
        conveyBelt[0][0] = leftBottomCorner;
        conveyBelt[1][n-1] = rightTopCorner;

    }
    public static void moveToRight() {
        rightTopCorner = conveyBelt[0][n-1];
        for(int i = n-1; i >=1; i--) {
            conveyBelt[0][i] = conveyBelt[0][i-1];
        }

    }
    public static void moveToLeft() {
        leftBottomCorner = conveyBelt[1][0];
        for(int i = 0; i < n-1; i++) {
            conveyBelt[1][i] = conveyBelt[1][i+1];
        }
    }
}



