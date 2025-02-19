
import java.util.*;

public class Main {

  static int[] arr = new int[5];

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int total = 0;
    for (int i = 0; i < 5; i++) {
      arr[i] = sc.nextInt();
      total += arr[i];
    }
    int minDiff = Integer.MAX_VALUE;
    for (int i = 0; i < 5; i++) {
      for (int j = i + 1; j < 5; j++) {
        for (int a = j + 1; a < 5; a++) {
          for (int b = a + 1; b < 5; b++) {
            int teamA = arr[i] + arr[j];
            int teamB = arr[a] + arr[b];
            int teamC = total - teamA - teamB;
            if (teamA != teamB && teamB != teamC && teamA != teamC) {
              minDiff = Math.min(minDiff, Math.max(teamA, Math.max(teamB, teamC)) - Math.min(teamA,
                  Math.min(teamB, teamC)));
            }
          }
        }
      }
    }
    minDiff = minDiff == Integer.MAX_VALUE ? -1 : minDiff;
    System.out.print(minDiff);
  }

}
