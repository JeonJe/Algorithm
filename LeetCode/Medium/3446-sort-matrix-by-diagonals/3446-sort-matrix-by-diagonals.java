import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

class Solution {

  public int[][] sortMatrix(int[][] grid) {
    int n = grid.length;
    if (n == 0) return new int[0][0];
    
    int[][] answer = new int[n][n];

    for (int startRow = n - 1; startRow >= 0; startRow--) {
      processDiagonal(grid, answer, startRow, 0, /*ascending=*/false);
    }

    for (int startCol = 1; startCol < n; startCol++) {
      processDiagonal(grid, answer, 0, startCol, /*ascending=*/true);
    }

    return answer;
  }

  private void processDiagonal(int[][] grid, int[][] answer, int r, int c, boolean ascending) {
    int n = grid.length;

    List<Integer> diag = new ArrayList<>();
    int i = r, j = c;
    while (i < n && j < n) {
      diag.add(grid[i][j]);
      i++; j++;
    }

    List<Integer> sorted = diag.stream()
        .sorted(ascending ? Comparator.naturalOrder() : Comparator.reverseOrder())
        .collect(Collectors.toList());

    i = r; j = c;
    int k = 0;
    while (i < n && j < n) {
      answer[i][j] = sorted.get(k++);
      i++; j++;
    }
  }
}