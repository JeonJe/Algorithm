import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        System.out.print(recursive(n));

    }

    public static int recursive(int n) {
        if( n == 1 ) {
            return 1;
        }
        return n + recursive(n-1);
    }


}