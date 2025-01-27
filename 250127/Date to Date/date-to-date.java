
import java.util.*;

public class Main {

  static int[] numOfDays = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int startMonth = sc.nextInt();
    int startDay = sc.nextInt();
    int endMonth = sc.nextInt();
    int endDay = sc.nextInt();

    int days1 = calculateDays(startMonth, startDay);
    int days2 = calculateDays(endMonth, endDay);
    System.out.println(days2 - days1 + 1);

  }

  private static int calculateDays(int startMonth, int startDay) {
    int days = 0;
    for (int i = 0; i < startMonth; i++) {
      days += numOfDays[i];
    }
    days += startDay;
    return days;
  }

}

