import java.io.*;
import java.util.*;

public class BOJ_1037 {
  public static void main(String[] args) throws Exception{
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(reader.readLine());
    StringTokenizer st = new StringTokenizer(reader.readLine());
    int[] seq = new int[N];
    for (int i  = 0; i < N; i++){
      seq[i] = Integer.parseInt(st.nextToken());
    }
    
    Arrays.sort(seq);
    int minValue = seq[0];
    int maxValue = seq[N-1];

    System.out.println(minValue*maxValue);
  }입
}
