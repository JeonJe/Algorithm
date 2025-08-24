class Solution {

  public int longestSubarray(int[] nums) {
    int left = 0;
    int zeroCount = 0;
    int answer = 0;

    for (int right = 0; right < nums.length; right++) {
      if (nums[right] == 0) {
        zeroCount++;
      }

      //슬라이딩 윈도우에 대해 0 의 개수 체크 
      while (zeroCount > 1) {
        if (nums[left] == 0) {
          zeroCount--;
        }
        left++;
      }

      answer = Math.max(answer, right - left);
    }
    return answer;
  }
}
