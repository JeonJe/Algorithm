import java.util.*;
import java.io.*;

public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int K = Integer.parseInt(st.nextToken());

    int[]seq = new int[N];
    st = new StringTokenizer(br.readLine());

    for (int i = 0; i < N; i++) {
      seq[i] = Integer.parseInt(st.nextToken());
    }

    int left = 0;
    int right = 0;
    int maxValue = 0;
    Map<Integer, Integer> dict = new HashMap<Integer, Integer>();

    while (left <= right && right < N) {
      int rightIdxFreq = dict.getOrDefault(seq[right],0);
      int leftIdxFreq = dict.getOrDefault(seq[left],0);
      if (rightIdxFreq < K) {
        dict.put(seq[right], rightIdxFreq+1);
        right++;
      } else {
        dict.put(seq[left], leftIdxFreq-1);
        left++;
      }
      maxValue = Math.max(maxValue, right-left);
    }

    System.out.println(maxValue);
  }
  
}
