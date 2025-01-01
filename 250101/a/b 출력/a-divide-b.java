import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        double division = (double) a / b;
        double factor = Math.pow(10, 21);
        double floored = Math.floor(division * factor) / factor;
        
        String result = Double.toString(floored);
        
        int dotIndex = result.indexOf(".");
        if (dotIndex == -1) {
            result += ".";
            dotIndex = result.indexOf(".");
        }
        
        int decimalPlaces = result.length() - dotIndex - 1;
        while (decimalPlaces < 20) {
            result += "0"; 
            decimalPlaces++;
        }
        System.out.println(result);







    }
}