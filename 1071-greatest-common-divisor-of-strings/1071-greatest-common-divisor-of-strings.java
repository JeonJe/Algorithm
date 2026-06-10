import java.util.*;

class Solution {
    public String gcdOfStrings(String str1, String str2) {
        String answer = ""; 

        for (int i = 0; i < str1.length(); i++) {
            String cur = str1.substring(0, i + 1);
            
            String temp1 = str1;
            String temp2 = str2;

            String check1 = temp1.replace(cur, "");
            String check2 = temp2.replace(cur, "");
            
            if(check1.equals("") && check2.equals("")) {
                answer = cur;
            }

        }

        return answer;
    }
}