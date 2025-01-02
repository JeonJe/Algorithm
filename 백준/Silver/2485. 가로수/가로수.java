

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] points = new int[n];
        for(int i = 0; i < n; i++) {
            points[i] = sc.nextInt();
        }

        int currentGcd = points[1] - points[0];
        for(int i = 1; i < n; i++) {
            currentGcd = gcd(currentGcd, points[i] - points[i - 1]);
        }

        int totalDistance = points[n - 1] - points[0];
        int totalTrees = (totalDistance / currentGcd) + 1;
        int additionalTrees = totalTrees - n;

        System.out.println(additionalTrees);

    }


    public static int gcd(int a, int b) {
        int minValue = Math.min(a, b);
        int maxValue = Math.max(a, b);
        if (minValue == 0) {
            return maxValue;
        }
        return gcd(minValue, maxValue % minValue);
    }


}