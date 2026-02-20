import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        char[] chars = input.toCharArray();
        Arrays.sort(chars);
        String sortedStr = new String(chars);
        System.out.println(sortedStr);
    }
}