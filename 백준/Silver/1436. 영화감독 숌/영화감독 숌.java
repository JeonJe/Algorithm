import java.util.*;
import java.io.*;

public class Main {

  public static void main(String[] args) throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());

    int curVal = 666;
    int count = 0;

    while (count < n) {
      if (String.valueOf(curVal).contains("666")) {
        count++;
      }
      curVal++;
    }
    System.out.println(curVal - 1);
  }

}
