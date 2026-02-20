

import java.util.*;

public class Main {
    public static void swap(IntWrapper a, IntWrapper b) {
        int temp = a.value;
         a.value = b.value;
         b.value = temp;
    }
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        IntWrapper a = new IntWrapper(n);
        IntWrapper b= new IntWrapper(m);
        swap(a, b);
        System.out.printf("%d %d", a.value, b.value);


    }

    public static class IntWrapper {
        Integer value;

        IntWrapper(int num) {
            value = num;
        }
    }
}