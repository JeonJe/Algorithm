
import java.util.*;

public class Main {

  static int[] firstCombi;
  static int[] secondCombi;
  static Set<int[]> set = new HashSet<>();
  static int n = 0;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    firstCombi = new int[3];
    for (int i = 0; i < 3; i++) {
      firstCombi[i] = sc.nextInt();
    }

    secondCombi = new int[3];
    for (int i = 0; i < 3; i++) {
      secondCombi[i] = sc.nextInt();
    }

    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        for (int k = 1; k <= n; k++) {
          if (isValidCombo(i, j, k, firstCombi) ||
              isValidCombo(i, j, k, secondCombi)) {
            set.add(new int[]{i, j, k});
          }
        }
      }
    }
    System.out.println(set.size());


  }

  private static boolean isValidCombo(int x, int y, int z, int[] combo) {
    return isDistanceValid(x, combo[0]) &&
        isDistanceValid(y, combo[1]) &&
        isDistanceValid(z, combo[2]);
  }

  private static boolean isDistanceValid(int a, int b) {
    int distance = Math.abs(a - b);
    distance = Math.min(distance, n - distance);
    return distance <= 2;
  }
}
