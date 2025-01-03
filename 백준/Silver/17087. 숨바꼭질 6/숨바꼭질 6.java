

import java.util.Arrays;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int[] arr = new int[n + 1];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        arr[n] = s;

        Arrays.sort(arr);

        int currentGcd = arr[1] - arr[0];
        for (int i = 2; i < n + 1; i++) {
            currentGcd = gcd(currentGcd, arr[i] - arr[i - 1]);
        }
        System.out.println(currentGcd);

    }

    private static int gcd(int a, int b) {
        if (a < b) {
            int temp = a;
            a = b;
            b = temp;
        }
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

}



