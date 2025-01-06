
import java.util.*;

public class Main {

        public static boolean isExceptYear(int y) {
            return (y % 100 == 0) && (y % 400 != 0);
        }
        public static boolean isSatisfied(int y) {
            if(isExceptYear(y)) {
                return false;
            }
            return y % 4 == 0;
        }
        public static void main(String[] args) {
            // Please write your code here.
            Scanner sc = new Scanner(System.in);
            int y = sc.nextInt();

            if(isSatisfied(y)) {
                System.out.print("true");
                return ;
            }

            System.out.print("false");

        }
}