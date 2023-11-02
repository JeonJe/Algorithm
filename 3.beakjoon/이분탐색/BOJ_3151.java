import java.io.*;
import java.util.*;

class BOJ_3151 {
  static int n;
  static int[] seq;
  static int[] mark;
  public static void main(String[] args) throws Exception {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    n = Integer.parseInt(reader.readLine());
    seq = new int[n];
    mark = new int[20000];
    StringTokenizer st = new StringTokenizer(reader.readLine());
    
    for (int i = 0; i < n; i++) {
      seq[i] = Integer.parseInt(st.nextToken());
    }
    Arrays.sort(seq);
    System.out.println(Arrays.toString(seq));
    int left = 0;
    int right = n;

    while (left+1 < right) {
      int mid = left + (left + right) / 2;

      if (check(mid)) {
        left = mid;
      } else {
        right = mid;
      }
      
    }
    System.out.println(left);
    
  }
  static boolean check(int mid) {
    //3팀원의 코딩실력 합이 0 
    return true;
  }
}