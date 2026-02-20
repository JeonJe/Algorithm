import java.util.*;

public class Main {

    public static boolean isContainThreeOrSixOrNine(int n) {
        String numToString = String.valueOf(n);
        return numToString.contains("3") || numToString.contains("6") || numToString.contains("9");
    }
    public static boolean isSatisfied(int n) {
        return n % 3 == 0  || isContainThreeOrSixOrNine(n);
    }
    
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();


        int count = 0;
        for(int i = a; i <= b; i++) {
            if(isSatisfied(i)) {
                count++;
            }
        }

        System.out.println(count);

    }
}