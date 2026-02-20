import java.util.*;

public class Main {
    static int[][] board = new int[201][201];
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i < 201; i++){
            Arrays.fill(board[i], 0);
        }
        
        int n = sc.nextInt();
        
        for(int i = 0; i < n; i++){
            int leftBottomX = sc.nextInt() + 100;
            int leftBottomY = sc.nextInt() + 100;
            int rightTopX = sc.nextInt() + 100;
            int rightTopY = sc.nextInt() + 100;

            draw(leftBottomX, leftBottomY, rightTopX, rightTopY);

        }

        int result = 0;
        for(int i = 0; i < 201; i++) {
            for(int j = 0; j < 201; j++) {
                if(board[i][j] > 0) {
                    result++;
                }
            }
        }
        System.out.print(result);
    }

    public static void draw(int x1, int y1, int x2, int y2) {
        for(int i = x1; i < x2; i++) {
            for(int j = y1; j < y2; j++) {
                board[i][j] = 1;
            }
        }
    }
}