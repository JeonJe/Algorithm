import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int x = sc.nextInt();
    int y = sc.nextInt();

    int count = 0;
    for (int curNumer = x; curNumer <= y; curNumer++) {
      if (isInstresting(curNumer)) {
        count++;
      }
    }
    System.out.println(count);
  }

  private static boolean isInstresting(int curNumer) {
    int firstDigit = curNumer % 10;
    int firstDigitCount = 0;
    int otherDigitCount = 0;
    Set<Integer> digits = new HashSet<>();

    while (curNumer > 0) {
      digits.add(curNumer % 10);
      if (firstDigit == curNumer % 10) {
        firstDigitCount++;
      } else {
        otherDigitCount++;
      }
      curNumer /= 10;
    }
    return (digits.size() == 2) && (firstDigitCount == 1 || otherDigitCount == 1);
  }
}
