import java.util.*;
import java.io.*;

public class Main {
  public static void main(String[] args) throws Exception {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(reader.readLine());
    int height = Integer.parseInt(st.nextToken());
    int width = Integer.parseInt(st.nextToken());

    int[]blocks = new int[width];

    st = new StringTokenizer(reader.readLine());

    for (int i = 0; i < width; i++) {
      blocks[i] = Integer.parseInt(st.nextToken());
    }

    int answer = 0;
    for (int i = 0; i < width; i++) {
      // i를 기준으로 왼쪽
      int leftMax = blocks[i];
      int rightMax = blocks[i];
      for (int j = 0; j < i; j++) {
        leftMax = Math.max(leftMax, blocks[j]);
      }
      // i를 기준으로 오른쪽
      for (int j = i; j < width; j++) {
        rightMax = Math.max(rightMax, blocks[j]);
      }
      int minMax = Math.min(leftMax, rightMax);
      answer += minMax - blocks[i];
    }
    System.out.println(answer);

  }
}
