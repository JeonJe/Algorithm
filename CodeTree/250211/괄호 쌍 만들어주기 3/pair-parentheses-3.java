import java.util.Scanner;

public class Main {
    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();

        int count = 0;
        for(int i = 0; i < input.length()-1; i++) {
            for(int j = i+1; j < input.length(); j++) {
                if(input.charAt(i) == '(' && input.charAt(j) == ')') {
                    count++;
                }

            }
        }
        System.out.println(count);
    }
}