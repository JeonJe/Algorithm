import java.util.*;
import java.io.*;

public class BOJ_2435 {
  public static void main(String[] args) throws Exception {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(rd.readLine());
    int n=0;
    int k=0;

    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());
    
    int[] seq = new int[n];

    st = new StringTokenizer(rd.readLine());
    for (int i = 0; i < n; i++) {
      seq[i] = Integer.parseInt(st.nextToken());
    }
    int answer = -1234567;
    int left = 0, right = 0;
    int cnt = 0;
    int sumTemp = 0;
    while (left <= right && right < n) {
      
      while(cnt < k) {
        sumTemp += seq[right];
        right++;
        cnt++;
      }
      answer = Math.max(answer, sumTemp);
      sumTemp -= seq[left];
      left++;
      cnt--;
    }
    System.out.println(answer);
  }
}
