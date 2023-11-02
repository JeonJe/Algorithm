import java.util.*;
import java.io.*;

public class BOJ_2012 {
  public static void main(String[] args) throws Exception {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(reader.readLine());
    int[] seq = new int[n];
    for (int i = 0; i < n; i++) {
      seq[i] = Integer.parseInt(reader.readLine());
    }

    Arrays.sort(seq);
    long answer = 0L;

    for (int i = 0; i < seq.length; i++) {
      answer += Math.abs(seq[i] - (i+1));
    }

    System.out.println(answer);

  }
}