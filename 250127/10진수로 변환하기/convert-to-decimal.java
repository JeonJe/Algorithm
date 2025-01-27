import java.util.*;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String binary = sc.next();

    int result = convertToHex(binary);
    System.out.println(result);
  }

  private static int convertToHex(String binary) {
    char[] charArray = binary.toCharArray();
    int num = 0;
    for (char c : charArray) {
      num = (num * 2) + Character.getNumericValue(c);
    }
    return num;
  }
}

