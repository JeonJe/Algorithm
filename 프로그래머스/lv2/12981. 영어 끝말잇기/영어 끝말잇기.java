import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        int round =0 ,idx = 0;
        
        Map<String, Integer> map = new HashMap<String, Integer>();
        
        String prev = words[0];
        map.put(prev, 1);
        
        for (int i = 1; i < words.length; i++) {
            int current_round = (int)(i / n);
            int current_order = i % n;
            String current_word = words[i];
            
            
            //현재 word가 이전에 나왔는지 확인
            if (map.containsKey(words[i]) || words[i].charAt(0) != prev.charAt(prev.length()-1) 
               || current_word.length() <= 1){
                answer[0] = current_order+1;
                answer[1] = current_round+1;
                break;
            }
            map.put(words[i], 1);
            prev = words[i];
                
        }
        
        return answer;
    }
}