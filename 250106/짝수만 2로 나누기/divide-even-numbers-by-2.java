
import java.util.*;

public class Main {

    public static void devide(Integer[] arr) {
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] % 2 == 0 ) {
                arr[i] = arr[i] / 2;
            }
        }
    }
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); 
        Integer[] arr = new Integer[N];
        for(int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        devide(arr);
        for(int i = 0; i < N; i++) {
            System.out.print(arr[i] + " ");

        }


    }
}