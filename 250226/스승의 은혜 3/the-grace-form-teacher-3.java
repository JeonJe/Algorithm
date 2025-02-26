import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {

  static int n;
  static int budget;
  static int[][] priceAndShipment;
  static int numerOfPerson;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    budget = sc.nextInt();

    priceAndShipment = new int[n][2];

    for(int i = 0; i < n; i++) {
      int price = sc.nextInt();
      int shipment = sc.nextInt();
      priceAndShipment[i][0] = price;
      priceAndShipment[i][1] = shipment;
    }

    for(int i = 0; i < n; i++) {
      applyDiscount(i);
    }

    System.out.println(numerOfPerson);

  }

  private static void applyDiscount(int target) {
    int[][] temp = priceAndShipment.clone();
    int tempBudget = budget;

    temp[target][0] = temp[target][0] / 2;

    Arrays.sort(temp, Comparator.comparing((int[] arr) -> arr[0])
        .thenComparing((int[] arr) -> arr[1]));

    int countPerson = 0;
    for(int i = 0; i < n; i++) {
      int totalPrice = temp[i][0] + temp[i][1];
      if(tempBudget - totalPrice >= 0) {
        tempBudget -= totalPrice;
        countPerson++;
      }
    }
    numerOfPerson = Math.max(numerOfPerson, countPerson);
  }
}
