

import java.util.*;

public class Main {

  public static int[] monthOfDays = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  public static String[] weekOfDays = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int startMonth = sc.nextInt();
    int startDay = sc.nextInt();
    int endMonth = sc.nextInt();
    int endDay = sc.nextInt();
    String targetWeekOfDay = sc.next();

    int diff = calculate(startMonth, startDay, endMonth, endDay);
    int countOfWeeks = diff / 7;
    int remain = diff % 7;
    
    for(int i = 1; i <= remain; i++) {
      if (weekOfDays[i].equals(targetWeekOfDay)) {
        countOfWeeks++;
      }
    }
    
    System.out.println(countOfWeeks);
  }

  public static int calculate(int m1, int d1, int m2, int d2) {
    int days1 = countDays(m1, d1);
    int days2 = countDays(m2, d2);

    return days2 - days1;
  }

  private static int countDays(int m1, int d1) {
    int count = 0;
    for(int i = 1; i < m1; i++) {
      count += monthOfDays[i];
    }
    count += d1;
    return count;
  }


}
