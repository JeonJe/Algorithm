import java.util.*;
import java.io.*;

class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer = 1;

        int left = Math.min(a,b);
        int right = Math.max(a,b);
        
        while (!match(left, right)) {
            answer++;
            left = left % 2 == 0? (int)(left / 2) : (int)(left / 2)+1;
            right = right % 2 ==0? (int)(right / 2) : (int)(right / 2)+1;
            
        }

        return answer;
    }
    
    public static boolean match(int a, int b){
        if (a % 2 == 0){
            return false;
        } else{
            if (a+1 == b){
                return true;
            } else{
                return false;
            }
        }
    }
}