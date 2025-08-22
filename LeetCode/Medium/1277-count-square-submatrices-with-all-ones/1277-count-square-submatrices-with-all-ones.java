class Solution {
    public int countSquares(int[][] matrix) {
        int n = matrix.length, m = matrix[0].length;
        //dp[i][j] -> (i,j)로 끝나는 정사각형의 개수
        int[][] dp = new int[n][m];
        int answer = 0;

        // 첫번째 행 
        for(int j = 0; j < m; j++) {
            dp[0][j] = matrix[0][j];
        }

        //첫번째 열 
        for(int i = 0; i < n; i++) {
            dp[i][0] = matrix[i][0];
        }

        for(int i = 1; i < n; i++) {
            for(int j = 1; j < m; j++) {
                if(matrix[i][j] == 1) {
                    // 크기 1의 사각형(i,j) + 이전 좌표들의 사각형 크기 중 가장 작은 값 
                    dp[i][j] = 1 + Math.min(dp[i-1][j], Math.min(dp[i][j-1], dp[i-1][j-1]));
                }
            }
        }
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                answer += dp[i][j];
            }
        }

       return answer;
    }
}