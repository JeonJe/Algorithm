import java.util.*;
import java.math.BigDecimal;
import java.math.RoundingMode;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        BigDecimal dividend = new BigDecimal(a);
        BigDecimal divisor = new BigDecimal(b);
     BigDecimal result = dividend.divide(divisor, 20, RoundingMode.DOWN);
        
System.out.println(result.toPlainString());







    }
}