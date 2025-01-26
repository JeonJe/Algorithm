import java.util.*;


public class Main {

    static int count = 0;
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        F(n);
    }

    public static void F(int num) {
        if(num == 1) {
            System.out.print(count);
            return;
        }

        count++;
        if(num % 2 == 0) {
            F(num / 2);
        } else { 
            F(num / 3);
        }
    }
}