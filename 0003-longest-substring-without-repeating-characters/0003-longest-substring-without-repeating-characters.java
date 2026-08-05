import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {

        if (s.isEmpty()) {
            return 0;
        }

        int answer = 1;
        int left = 0;

        Set<Character> temp = new HashSet<>();
        temp.add(s.charAt(0));

        for (int right = 1; right < s.length(); right++) {

            //새 문자가 set에 있으면?
            if (temp.contains(s.charAt(right))) {
                // 사라질때까지 s[left]를 set에서 빼며 left를 전진시킨다.
                while (temp.contains(s.charAt(right))) {
                    temp.remove(s.charAt(left));
                    left++;
                }
            }

            //set에 새문자를 넣고. 길이를 갱신한다
            temp.add(s.charAt(right));
            answer = Math.max(answer, right - left + 1);
        }

        return answer;
    }
}
