import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요
        Scanner sc = new Scanner(System.in);
        String[] inputs = sc.nextLine().split(" ");        
        int a = Integer.parseInt(inputs[0]);
        int b = Integer.parseInt(inputs[1]);    
        int c = Integer.parseInt(inputs[2]);

        int sum = a+b+c;
        System.out.println(sum);
        int avg = sum / 3;
        System.out.println(avg);
        System.out.println(sum-avg);


    }
}