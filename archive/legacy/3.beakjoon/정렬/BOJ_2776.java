import java.util.*;
import java.io.*;

public class BOJ_2776 {
  public static void main(String[] args) throws Exception {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    int T = Integer.parseInt(reader.readLine());
    StringBuilder answer = new StringBuilder();

    for (int i = 0; i < T; i++) {

      HashSet<Integer> hs = new HashSet<>();

      int N = Integer.parseInt(reader.readLine());
      st = new StringTokenizer(reader.readLine());

      while (st.hasMoreTokens()) {
        int num = Integer.parseInt(st.nextToken());
        hs.add(num);
      }

      int M = Integer.parseInt(reader.readLine());
      st = new StringTokenizer(reader.readLine());
      while (st.hasMoreTokens()) {
        int num = Integer.parseInt(st.nextToken());
        if (hs.contains(num)) {
          answer.append("1\n");
        } else{
          answer.append("0\n");
        }
      }
    
      //TC
    }
    System.out.println(answer.toString());
    
  }
}
