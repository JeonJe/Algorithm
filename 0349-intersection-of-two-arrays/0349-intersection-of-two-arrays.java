import java.io.IOException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        
        int[] temp = new int[1000];
        int cnt = 0;
        int i = 0;
        int j = 0;
        
        Arrays.sort(nums1);
        Arrays.sort(nums2);

        while (i < nums1.length && j < nums2.length){
            if(nums1[i] < nums2[j]){
                i++;
                while(i < nums1.length && nums1[i-1] == nums1[i]){
                    i++;
                }
                
            } else if (nums1[i] > nums2[j]){
                j++;
                while(j < nums2.length && nums2[j-1] == nums2[j] ){
                    j++;
                }
            } else {
                temp[cnt] = nums1[i];
                cnt++;
                i++;
                while(i < nums1.length && nums1[i-1] == nums1[i]){
                    i++;
                }
                j++;
                while(j < nums2.length && nums2[j-1] == nums2[j] ){
                    j++;
                }
            }
        }
        int[] answer = new int[cnt];
        int answerIndex = 0;

        for (int same : temp) {
            if (same > 0){
                answer[answerIndex] = same;
                answerIndex++;
            }
        }
        return answer;

    }
}