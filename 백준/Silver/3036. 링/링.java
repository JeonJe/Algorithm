
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];

        for(int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }

        for(int i = 1; i < n; i++){
            int l = lcm(nums[0], nums[i]);
            System.out.printf("%d/%d%n", l / nums[i], l / nums[0]);
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