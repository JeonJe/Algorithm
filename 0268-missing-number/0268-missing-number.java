
class Solution {
    public int missingNumber(int[] nums) {

        int[] checkNums = new int[nums.length+2];

        for(int i = 0; i < nums.length; i++){
            checkNums[nums[i]] += 1;
        }

        for(int i = 0; i < nums.length+2; i++){
            if(checkNums[i] == 0) {
                return i;
            }
        }
        return 0;
    }
}