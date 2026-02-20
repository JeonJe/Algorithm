import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] arr = new int[n];

        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);
        for(Integer e : arr) {
            System.out.print(e + " ");
        }
        System.out.println();

        Integer[] integerArr = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        Arrays.sort(integerArr, Collections.reverseOrder());

        for(Integer e : integerArr) {
            System.out.print(e + " ");
        }
    }
}