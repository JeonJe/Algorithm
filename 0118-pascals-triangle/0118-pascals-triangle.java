import java.util.ArrayList;
import java.util.List;

class Solution {
  public List<List<Integer>> generate(int numRows) {
    int[][] arr = new int[31][31];

    for(int j = 0; j <= numRows; j++) {
      arr[0][j] = 1;
    }

    for(int i = 0; i <= numRows; i++) {
      arr[i][0] = 1;
    }

    List<List<Integer>> answer = new ArrayList<>();
    for(int i = 1; i <= numRows; i++) {
      answer.add(new ArrayList<>());
      answer.get(i - 1).add(1);
      for(int j = 1; j < i; j++) {
        arr[i][j] = arr[i-1][j] + arr[i-1][j-1];
        answer.get(i-1).add(arr[i][j]);
      }
    }
    return answer;
  }
}
