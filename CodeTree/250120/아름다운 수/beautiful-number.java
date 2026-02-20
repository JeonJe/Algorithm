

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;

class Main {

  static int n = 0;
  static List<Integer> nums = new ArrayList<>();
  static int count = 0;

  public static void main(String[] args) {

    Scanner scanner = new Scanner(System.in);
    n = scanner.nextInt();

    dfs(0);

    System.out.println(count);

  }

  //n 자리 조합 만들기
  private static void dfs(int depth) {
    if (depth == n) {
      if (isBeaultifule()) {
        count++;
      }
      return;
    }

    for (int i = 1; i <= 4; i++) {
      nums.add(i);
      dfs(depth + 1);
      nums.remove(nums.size() - 1);
    }
  }

  //아름다운 수 판별
  private static boolean isBeaultifule() {
    for (int i = 0; i < n; i += nums.get(i)) {
      //현재 수로 아름다운수를 만들려고 할 때 범위가 넘어가는 경우
      if (i + nums.get(i) > n) {
        return false;
      }
      //현재 수만큼 반복하면서 같은 수인지 확인
      for(int j = 0; j < nums.get(i); j++) {
        if(!Objects.equals(nums.get(i), nums.get(i + j))) {
          return false;
        }
      }

    }
    return true;
  }

}



