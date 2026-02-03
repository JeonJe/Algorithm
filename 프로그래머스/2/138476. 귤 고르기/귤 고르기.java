import java.util.*;

class Solution {
     int solution(int k, int[] tangerine) {
        int answer = 0;

        int[] count = new int[10_000_001];
        for (int num : tangerine) {
            count[num]++;
        }

        Arrays.sort(count);
        for (int i = count.length - 1; i >= 0; i--) {
            answer++;
            k -= count[i];
            if (k <= 0) {
                break;
            }
        }
        return answer;
    }
}