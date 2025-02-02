
import java.util.*;

public class Main {

  static int MAX_BOARD_SIZE = 2000;
  public static int[] arr = new int[MAX_BOARD_SIZE];

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int numOfCommand = sc.nextInt();

    int curPosition = 1;
    for (int i = 0; i < numOfCommand; i++) {
      int numOfFlip = sc.nextInt();
      String dir = sc.next();
      if (dir.equals("R")) {
        for (int j = curPosition; j < curPosition + numOfFlip; j++) {
          arr[j] = 1;
        }
        curPosition = curPosition + numOfFlip - 1;
      }

      if (dir.equals("L")) {
        for (int j = curPosition; j > curPosition - numOfFlip; j--) {
          arr[j] = -1;
        }
        curPosition = curPosition - numOfFlip + 1;
      }
    }

    int white = 0;
    int black = 0;
    for (int i = 0; i < MAX_BOARD_SIZE; i++) {
      if (arr[i] == -1) {
        white++;
      }
      if (arr[i] == 1) {
        black++;
      }
    }

    System.out.printf("%d %d", white, black);

  }

}
