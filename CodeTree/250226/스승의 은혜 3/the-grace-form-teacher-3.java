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

    for (int i = 0; i < n; i++) {
      int price = sc.nextInt();
      int shipment = sc.nextInt();
      priceAndShipment[i][0] = price;
      priceAndShipment[i][1] = shipment;
    }

    Arrays.sort(priceAndShipment,
        Comparator.comparing(arr -> arr[0] + arr[1])
    );

    for (int i = 0; i < n; i++) {
      int disCountPrice = priceAndShipment[i][0] / 2;
      priceAndShipment[i][0] = disCountPrice;
      int count = getCountPerson(priceAndShipment, budget);
      numerOfPerson = Math.max(numerOfPerson, count);
      priceAndShipment[i][0] = priceAndShipment[i][0] * 2;
    }

    System.out.println(numerOfPerson);

  }
  private static int getCountPerson(int[][] temp, int budget) {
    int countPerson = 0;
    for (int i = 0; i < n; i++) {
      int totalPrice = temp[i][0] + temp[i][1];
      if (budget - totalPrice >= 0) {
        budget -= totalPrice;
        countPerson++;
      }
    }
    return countPerson;
  }
}
