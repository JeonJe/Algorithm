class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        
        while (s.length() > 1){
            answer[0] ++;
            int numOfOne = 0;
            for(int i = 0; i < s.length(); i++){
                char cur = s.charAt(i);
                if (cur == '0'){
                    answer[1]++;
                } else {
                    numOfOne++;
                }
            }
            s = Integer.toString(numOfOne,2);
            
        }
            //temp의 2진법이 s가 됨 
        return answer;
    }
}