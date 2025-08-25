class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int m = mat.length;
        if (m == 0) return new int[0];
        int n = mat[0].length;
        int[] res = new int[m * n];

        int i = 0, j = 0, dir = 1; // 1: up-right, -1: down-left
        for (int k = 0; k < m * n; k++) {
            res[k] = mat[i][j];

            if (dir == 1) { // up-right
                if (j == n - 1) { // 오른쪽 끝 -> 아래로 이동, 방향 전환
                    dir *= -1;
                    i++;
                } else if (i == 0) { // 맨 위 -> 오른쪽으로 이동, 방향 전환
                    j++;
                    dir *= -1;

                } else { // 대각선 진행
                    j++;
                    i--;
                }
            } else { // dir == -1, down-left
                if (i == m - 1) { // 아래 끝 -> 오른쪽으로 이동, 방향 전환
                    j++;
                    dir *= -1;

                } else if (j == 0) { // 맨 왼쪽 -> 아래로 이동, 방향 전환
                    dir *= -1;
                    i++;
                } else { // 대각선 진행
                    i++;
                    j--;
                }
            }
        }

        return res;
    }
}