import java.util.Arrays;
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int answer = 0;
        int diff = Integer.MAX_VALUE;
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
        
        for (int cur = 0; cur < nums.length-2; cur++){
            int left = cur+1;
            int right = nums.length-1;
         
            
            while (left < right) {
               int threeSum = nums[cur]+nums[left]+nums[right];
                if(threeSum == target) {
                    return target;
                } else if(threeSum > target) {
                    right -= 1;
                } else {
                    left += 1;
                }
                if ( Math.abs(threeSum - target) < diff ) {
                    diff = Math.abs(threeSum - target);
                    answer = threeSum;
                }    
            }
            
        }
        return answer;
    }
}