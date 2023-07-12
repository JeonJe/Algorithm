import java.io.*;
import java.util.*;

public class Main {
  static int N, K;
  static int maxValue;
  public static void main(String[] args) throws Exception {

    // 구구단 N단 K항 까지 
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    K = Integer.parseInt(st.nextToken());

    maxValue = -1;
    
    for (int i = 1; i < K+1; i++) {
      String currentValue = String.valueOf(N*i);
      StringBuffer sb = new StringBuffer(currentValue);
      int reversedValue = Integer.parseInt(sb.reverse().toString());
      maxValue = Math.max(maxValue, reversedValue);
    }

    System.out.println(maxValue);
  
  }
}