import java.util.*;


class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int n = spells.length;
        int m = potions.length;

        int[] answer = new int[n];
        Arrays.sort(potions);

        for(int i = 0; i < n; i++) {
            double lowerPoint = (double) success / spells[i];

            int lowerIdx = lowerBound(potions, lowerPoint);
            answer[i] = m - lowerIdx;
        }

        return answer;

    }

    public int lowerBound(int[] arr, double target) {
        int left = 0;
        int right = arr.length; //없으면 끝 리턴

        while(left < right) {
            int mid = left + (right - left) / 2;
            if(arr[mid] >= target) {
                right = mid;
            } else {
                left = mid+1;
            }
        }
        return left;
    }
}