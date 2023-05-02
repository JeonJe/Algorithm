import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        while (n > 0){
            int q = n / 10;
            int r = n % 10;
            answer += r;
            n = q;
        }

        return answer;
    }
}