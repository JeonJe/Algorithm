import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        String[] inputs = sc.nextLine().split(" ");
        int a = Integer.parseInt(inputs[0]);
        int b = Integer.parseInt(inputs[1]);

        StringBuilder sb = new StringBuilder();
        for(int i = 1; i < b+1; i+=2) {
            sb.append(i + " ");
        }
        System.out.print(sb.toString());
    }
}