import java.util.*;

public class Main {
    static int n = 0;
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        printWord(0);
    }

    public static void printWord(int depth) {
        if(depth == n) {
            return;
        }
        System.out.println("HelloWorld");
        printWord(depth+1);

    }
}