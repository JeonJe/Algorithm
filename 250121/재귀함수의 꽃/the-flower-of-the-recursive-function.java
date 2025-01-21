import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        print(n);
    }

    public static void print(int n) {
        if(n == 0) {
            return ;
        }
        System.out.print(n + " ");
        print(n - 1);
        System.out.print(n + " ");
        
    }
}