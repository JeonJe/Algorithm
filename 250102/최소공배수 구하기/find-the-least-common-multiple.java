import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        System.out.print(lcm(Math.max(n,m), Math.min(n,m)));
    }

    public static int lcm(int a, int b) {
        return (a*b) / gcd(a,b);
    }

    public static int gcd(int a, int b) {
        if(b == 0) {
            return a;
        }

        int r = a % b;
        return gcd(b , r);
    }
}