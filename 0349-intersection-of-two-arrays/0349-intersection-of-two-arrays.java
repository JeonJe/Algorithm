import java.io.IOException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);

        Set<Integer> answer = new HashSet<>();

        for (int i : nums2) {
            if (Arrays.binarySearch(nums1, i) >= 0) {
                answer.add(i);
            }
        }
        
        Integer[] arr = answer.toArray(new Integer[0]);
        return Arrays.stream(arr).mapToInt(Integer::intValue).toArray();
    }
}