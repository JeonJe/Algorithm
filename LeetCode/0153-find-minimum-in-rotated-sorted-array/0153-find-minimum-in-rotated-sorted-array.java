class Solution {
    public int findMin(int[] nums) {
           int minNum = nums[0];
        int left = 0;
        int right = nums.length-1;

         while(left <= right) {
            if(nums[left] < nums[right]) {
                minNum = Math.min(minNum, nums[left]);
                break;
            }
            int mid = left + Math.floorDiv((right - left) , 2);
            minNum = Math.min(minNum, nums[mid]);
            if(nums[left] <= nums[mid]){
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return minNum;
    }
}