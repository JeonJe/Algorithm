import java.util.*;


public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int bigger = Math.max(n,m);
        int result = 1;

        for(int i = 1; i < bigger + 1; i++) {
 
            if(n % i == 0 &&  m % i== 0) {
                result = i;
            }
        }
        System.out.print(result);
    }
}