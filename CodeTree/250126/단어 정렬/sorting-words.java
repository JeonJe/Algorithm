import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        String[] strs = new String[n];

        for(int i = 0; i < n; i++) {
            strs[i] = sc.next();
        }
        
        Arrays.sort(strs);

        for(String s : strs) {
            System.out.println(s);
        }
    }
}