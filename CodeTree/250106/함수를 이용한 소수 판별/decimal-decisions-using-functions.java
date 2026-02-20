import java.util.*;

public class Main {

    public static boolean isPrime(int n) {
        if(n == 1) {
            return false;
        }
        
        for(int i = 2; i < n; i++) {
            if(n % i == 0) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        int sum = 0;
        int a = sc.nextInt();
        int b = sc.nextInt();

        for(int i = a; i <= b; i++) {
            if(isPrime(i)) {
                sum += i;
            }
        }

        System.out.println(sum);
    }
}