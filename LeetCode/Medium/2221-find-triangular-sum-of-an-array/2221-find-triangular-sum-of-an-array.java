class Solution {
    public int triangularSum(int[] nums) {
        int answer = 0;

        int n = nums.length;
        int[][] arr = new int[n][n];
        for(int i = 0; i < n; i++) {
            arr[0][i] = nums[i];
        }

        for(int i = 1; i < n; i++) {
            for(int j = 0; j < n-1; j++) {
                arr[i][j] = (arr[i-1][j] + arr[i-1][j+1]) % 10;
            }
        }

        return arr[n-1][0];
    }
}