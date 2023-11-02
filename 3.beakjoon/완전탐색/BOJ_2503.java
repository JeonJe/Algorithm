import java.io.*;
import java.util.*;

public class BOJ_2503 {
  static int [][]candidates;
  static boolean []visited;
  static int answer;

  public static void main(String[] args) throws Exception{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());

    candidates = new int[N][3];
    visited = new boolean[10];
    for (int i = 0; i < N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int j = 0; j < 3; j++) {
        candidates[i][j] = Integer.parseInt(st.nextToken());
      }
    }
    answer = 0;
    List<Integer> path = new ArrayList<>();
    dfs(0, path);

    System.out.println(answer);
  }

  public static void dfs(int depth, List<Integer> path) {
    if (path.size() >= 3) {
      if (check(path)) {
        answer++;
      }
      return ;
    }

    for (int i = 1; i < 10; i++) {
      if (!visited[i]){
        visited[i] = true;
        path.add(i);
        dfs(depth+1, path);
        path.remove(path.size()-1);
        visited[i] = false;
      }
    }
  }

  public static boolean check(List<Integer> path) {
    for (int[] candidate : candidates) {
      int num = candidate[0];
      int s = candidate[1];
      int b = candidate[2];

      int check_s = 0;
      int check_b = 0;

      String strNum = String.valueOf(num);
      List<Integer> listNum = new ArrayList<Integer>();

      for (char digitChar : strNum.toCharArray()) {
        int digit = Character.getNumericValue(digitChar);
        listNum.add(digit);
      }

      for (int i = 0 ; i < listNum.size() ; i++) {
        if(path.get(i) == listNum.get(i)) {
          check_s++;
        } else if(path.contains(listNum.get(i))) {
          check_b ++;
        }
      }

      if (check_s != s || check_b != b) {
        return false;
      }
    }

    return true;
  }
}
