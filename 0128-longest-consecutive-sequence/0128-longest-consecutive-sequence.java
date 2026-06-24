import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0 || nums.length == 1) {
            return nums.length;
        }
        
        int answer = 1;

        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        //시작점 찾기 
        for (Integer cur : set) {
            //시작점
            if (!set.contains(cur - 1)) {
                int right = cur;
                while (set.contains(right + 1)) {
                    right++;
                }
                answer = Math.max(answer, right - cur + 1);
               
            } else {

            }

        }

        return answer;
    }
}
