import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {

        int answer = 0;
        char[] charArray = s.toCharArray();

        for(int i = 0; i < charArray.length; i++) {

            StringBuilder sb = new StringBuilder();
            sb.append(charArray[i]);
            Set<Character> temp = new HashSet<>();
            temp.add(charArray[i]);

            for (int j = i + 1; j < charArray.length; j++) {
                if(temp.contains(charArray[j])) {
                    break;
                }

                temp.add(charArray[j]);
                sb.append(charArray[j]);
            }

            answer = Math.max(answer, sb.length());
        }

        return answer;
    }
}
