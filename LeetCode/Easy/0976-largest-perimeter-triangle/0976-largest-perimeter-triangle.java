import java.util.*;

class Solution {
    public int largestPerimeter(int[] nums) {
        
        Arrays.sort(nums);

        for(int i = nums.length - 1; i >= 2; i--) {
            int a = nums[i];
            int b= nums[i-1];
            int c = nums[i-2];

            //세 변으로 삼격형을 만들 수 있는 경우  b + c > a
            if(b + c > a) {
                return a + b + c;
            }

        }

        return 0; 
    }
}