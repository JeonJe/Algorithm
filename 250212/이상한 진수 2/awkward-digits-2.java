
import java.util.*;

public class Main {

  static int maxValue = 0;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String binary = sc.next();

    char[] charArray = binary.toCharArray();
    for(int i = 0; i < charArray.length; i++) {
      flip(charArray, i);
      toDecimal(charArray);
      flip(charArray, i);
    }
    System.out.println(maxValue);

  }

  private static void flip(char[] charArray, int i) {
    if(charArray[i] == '0') {
      charArray[i] = '1';
    } else {
      charArray[i] = '0';
    }
  }

  private static void toDecimal(char[] charArray) {
    int sum = 0;
    for(int i = 0; i < charArray.length; i++) {
      sum += (int) ((charArray[i] - '0') * Math.pow(2, charArray.length - 1 - i));
    }
    maxValue = Math.max(maxValue, sum);
  }
}
