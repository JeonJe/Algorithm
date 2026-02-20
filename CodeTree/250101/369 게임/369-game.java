import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
         
        for(int i = 1; i <= n; i++) {
            if(i % 3 == 0) {
                System.out.print("0 " );
            } else if(isContain(i)) {
                System.out.print("0 " );
            } else {
                System.out.print(i + " ");
            }
        }
    }

    private static boolean isContain(int i) {
           String[] targets = {"3", "6", "9"};
        String toString = String.valueOf(i);
        for(String target : targets) {
            if(toString.contains(target)){
                return true;
            }
        }
        return false;
    }
}