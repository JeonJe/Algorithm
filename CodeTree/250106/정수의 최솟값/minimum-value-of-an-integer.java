import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int minValue = find(a,b,c);
        System.out.println(minValue);

    }

    public static int find(int a, int b, int c) {
        return Math.min(Math.min(a,b), c);
    }
}