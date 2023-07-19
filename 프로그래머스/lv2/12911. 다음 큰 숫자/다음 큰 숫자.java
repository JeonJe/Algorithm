import java.util.*;

class Solution {
    
    public int solution(int n) {
        //n 을 2진수로 바꾸었을 때 1의 개수 
        int cntOneOfN = countOne(n);
        
        for (int i = n+1; i <=1000000; i++){
            if (countOne(i) == cntOneOfN) {
                return i;
            }
        }
        return -1;
    }
    
    public static int countOne(int n) {
        int cnt_one = 0;
        
        String binaryN = Integer.toString(n,2);
        for(int i = 0; i < binaryN.length(); i++){
            if(binaryN.charAt(i) == '1'){
                cnt_one++;
            }
        }
        return cnt_one;
    }
}