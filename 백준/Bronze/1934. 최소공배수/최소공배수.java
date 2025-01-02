import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for(int i = 0; i < n; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println(lcm(Math.max(a,b), Math.min(a,b)));
        }

    }

    public static int lcm(int a, int b) {
        return (a * b) / (gcd(a, b));
    }

    public static int gcd(int a, int b) {
        if (b == 0) {

            return a;
        }
        return gcd(b, a % b);
    }


}