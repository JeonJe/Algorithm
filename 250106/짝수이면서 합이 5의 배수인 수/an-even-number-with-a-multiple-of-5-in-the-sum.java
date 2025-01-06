import java.util.*;

public class Main {
    private static boolean isEvenAndFiveMultiple(int n) {
        if(n % 2 != 0) {
            return false;
        }
        int digitSum = 0;
        while (n > 0) {
            int q = n / 10;
            int r = n % 10;

            digitSum += r;
            n = q;
        }
        return digitSum % 5 == 0;

    }
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        if(isEvenAndFiveMultiple(n)) {
            System.out.print("Yes");
        } else {
            System.out.print("No");
        }
    }
}