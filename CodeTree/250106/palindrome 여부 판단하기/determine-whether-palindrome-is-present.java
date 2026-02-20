
import java.util.*;

public class Main {
    public static boolean isPalindrome(String n) {
        for(int i = 0; i < n.length()/2; i++) {
            if(n.charAt(i) != n.charAt(n.length()-1-i)) {
                return false;
            }
        }

        return true;


    }
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        if(isPalindrome(word)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }

}