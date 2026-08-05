import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {

        int answer = 0;
        int left = 0;

        Set<Character> temp = new HashSet<>();

        for (int right = 0; right < s.length(); right++) {

            // 사라질때까지 s[left]를 set에서 빼며 left를 전진시킨다.
            while (temp.contains(s.charAt(right))) {
                temp.remove(s.charAt(left));
                left++;
            }

            //set에 새문자를 넣고. 길이를 갱신한다
            temp.add(s.charAt(right));
            answer = Math.max(answer, right - left + 1);
        }

        return answer;
    }
}
