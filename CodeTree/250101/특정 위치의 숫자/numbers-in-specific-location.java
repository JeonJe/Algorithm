import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];

        String[] inputs = sc.nextLine().split(" ");
        for(int i = 0; i < 10; i++ ) {
            arr[i] = Integer.parseInt(inputs[i]);
        }

        System.out.print(arr[2] + arr[4] + arr[9]);
    }
}