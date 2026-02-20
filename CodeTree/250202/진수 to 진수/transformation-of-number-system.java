
import java.util.*;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
    int n = sc.nextInt();

    int decimalNumber = convertToDecimal(a, n);
    convertToBase(b, decimalNumber);
  }

  public static int convertToDecimal(int base, int n) {
    String stringValue = String.valueOf(n);
    int result = 0;

    for (int i = 0; i < stringValue.length(); i++) {
      result = result * base + Character.getNumericValue(stringValue.charAt(i));
    }
    return result;
  }

  public static void convertToBase(int base, int n) {
    int[] arr = new int[20];
    int count = 0;

    while (true) {
      if (n < base) {
        arr[count] = n;
        count++;
        break;
      }
      arr[count] = n % base;
      count++;
      n = n / base;
    }

    for (int i = count - 1; i >= 0; i--) {
      System.out.print(arr[i]);
    }
  }

}
