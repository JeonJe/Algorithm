import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        print1(n);
        System.out.println();
        print2(n);
    }

    public static void print1(int n) {
        if(n == 0) {
            return ;
        }
        print1( n - 1 );
        System.out.print(n + " ");
    } 

    public static void print2(int n) {
        if(n == 0) {
            return ;
        }
        System.out.print(n + " ");
        print2( n - 1 );
    }
    
}