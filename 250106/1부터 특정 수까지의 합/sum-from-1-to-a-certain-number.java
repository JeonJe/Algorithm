import java.util.*;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int num = print(N);
        System.out.println(num);

    }

    public static int print(int N) {
        int sum = 0;
        for(int i = 0; i <= N; i++) {
            sum += i;
        }
        return sum / 10;
    }
}