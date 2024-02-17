import java.io.IOException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        
        Set<Integer> answer = new HashSet<>();

        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int i = 0;
        int j = 0;

        while (i < nums1.length && j < nums2.length){
            if(nums1[i] < nums2[j]){
                i++;
            } else if (nums1[i] > nums2[j]){
                j++;
            } else {
                answer.add(nums1[i]);
                i++;
                j++;
            }
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}