import java.util.*;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        double a = 5.26;
        double b = 8.27;

        double product = a*b;

        System.out.printf("%.3f", Math.round(product * 1000) / 1000.0);
    }
}