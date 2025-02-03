import java.util.*;

public class Main {
    static int[] arr ;
    static int n;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
         n = scanner.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();

        }

        int minimumDistance = Integer.MAX_VALUE;
        for(int i = 0; i < n; i++) {
            int distance  = gatherAt(i);
            minimumDistance = Math.min(minimumDistance, distance);

        }
        System.out.print(minimumDistance);
    }

    public static int gatherAt(int houseNumber) {
        int totalDistance = 0;
        for(int i = 0; i < n; i++) {
            int distance = Math.abs(houseNumber - i);
            totalDistance += distance * arr[i];

        }
        return totalDistance;

    }

}