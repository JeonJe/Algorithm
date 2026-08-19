  class Solution {
      public int maxProduct(int[] nums) {
          int curMax = nums[0];
          int curMin = nums[0];
          int answer = nums[0];

          for (int i = 1; i < nums.length; i++) {
              int num = nums[i];
              int prevMax = curMax;

              curMax = Math.max(num, Math.max(prevMax * num, curMin * num));
              curMin = Math.min(num, Math.min(prevMax * num, curMin * num));

              answer = Math.max(answer, curMax);
          }
          return answer;
      }
  }
