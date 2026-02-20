import java.util.*;
import java.io.*;

public class BOJ_2304 {

  public static void main(String[] args) throws Exception {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(rd.readLine());
    StringTokenizer st;

    int[][] seq = new int[N][2];
    int indexOfMax = 0;
    int valueOfMax = 0;
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(rd.readLine());
      for (int j = 0; j < 2; j++) {
        seq[i][j] = Integer.parseInt(st.nextToken());
        if (seq[i][1] > valueOfMax){
          valueOfMax = seq[i][j];
          indexOfMax = seq[i][0];
        }
      }
    }

    Arrays.sort(seq, (o1, o2) -> {
      return o1[0] - o2[0];
    });
    int warehouseLength = seq[seq.length-1][0];
    int[] warehouse = new int[warehouseLength+1];
    for (int i = 0; i < seq.length; i++) {
      warehouse[seq[i][0]] = seq[i][1];
    }

    int left = 0;
    int left_max = 0;
    int right = warehouseLength;
    int right_max = 0;
    int answer = 0;

    while(left <= indexOfMax) {
      if (left_max < warehouse[left] ){
        left_max = warehouse[left];
      }
      answer += left_max;
      left++;
    }

    while(right > indexOfMax) {
      if (right_max < warehouse[right]) {
        right_max = warehouse[right];
      }
      answer += right_max;
      right--;
    }
    System.out.println(answer);

  }
  
}
