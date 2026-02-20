import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int startHour = sc.nextInt();
    int startMinute = sc.nextInt();
    int endHour = sc.nextInt();
    int endMinute = sc.nextInt();

    System.out.println(endHour * 60 + endMinute - startHour * 60 - startMinute);
  }

}

