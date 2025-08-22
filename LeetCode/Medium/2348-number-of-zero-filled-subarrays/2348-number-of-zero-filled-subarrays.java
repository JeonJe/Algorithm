class Solution {
    public long zeroFilledSubarray(int[] nums) {
        int left = 0, right = 0;
        int n = nums.length;
        long answer = 0;

        while(left < n) {
            right = left;
            if(nums[left] == 0) {
                int count = 1;
                while(right < n && nums[right] == 0) {
                    answer += count;
                    right++;
                    count++;
                }
                left = right;
            } else {
                left++;
            }
        }
        return answer;

    }
}