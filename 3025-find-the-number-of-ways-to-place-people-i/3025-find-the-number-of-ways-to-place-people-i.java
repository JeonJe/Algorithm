import java.util.*;
import java.util.stream.*;

class Solution {
  public int numberOfPairs(int[][] points) {
    // y 내림차순, y 같으면 x 오름차순
    int[][] pts = Arrays.stream(points)
        .sorted(Comparator.comparingInt((int[] a) -> a[1]).reversed()
                          .thenComparingInt(a -> a[0]))
        .toArray(int[][]::new);

    int n = pts.length;
    int ans = 0;

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (i == j) continue;

        int[] A = pts[i];
        int[] B = pts[j];

        // A is upper-left of B
        if (A[0] <= B[0] && A[1] >= B[1]) {
          boolean empty = true;

          // 사각형(경계 포함) 안에 A/B 이외의 점이 있는지 확인
          for (int k = 0; k < n; k++) {
            if (k == i || k == j) continue;
            int[] C = pts[k];
            if (C[0] >= A[0] && C[0] <= B[0] &&
                C[1] >= B[1] && C[1] <= A[1]) {
              empty = false;
              break;
            }
          }

          if (!empty) continue;
          ans++; 
        }
      }
    }

    return ans;
  }
}