import java.util.*;
import java.io.*;

public class Main {

  private static int answer = 0;
  private static int k = 0;
  private static int n = 0;
  private static int nLength = 0;
  private static String[] elements;

  public static void main(String[] args) throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    n = Integer.parseInt(st.nextToken());
    nLength = String.valueOf(n).length();

    k = Integer.parseInt(st.nextToken());

    elements = br.readLine().split(" ");

    StringBuilder sb = new StringBuilder();
    dfs(sb);

    System.out.println(answer);
  }

  private static void dfs(StringBuilder sb) {
    if (sb.length() > nLength) {
      return;
    }

    if (!sb.isEmpty()) {
      int curVal = Integer.parseInt(sb.toString());
      if (curVal <= n) {
        answer = Math.max(answer, curVal);
      }
    }

    for (int i = 0; i < k; i++) {
      sb.append(elements[i]);
      dfs(sb);
      sb.deleteCharAt(sb.length() - 1);
    }
  }

}
