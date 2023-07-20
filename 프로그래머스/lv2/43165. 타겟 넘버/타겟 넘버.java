import java.util.*;
import java.io.*;

class Solution {
    static int[] numArray;
    static int targetValue;
    static int answer = 0;
    
    public int solution(int[] numbers, int target) {
        
        numArray = numbers;
        targetValue = target;
        
        dfs(numArray[0],1);
        dfs(-1*numArray[0],1);
        
        return answer;
    }
    
    public static void dfs(int currentSum, int depth) {
        if( depth >= numArray.length ) {
            if (currentSum == targetValue) {
                answer++;    
            }
            return;
        }
        
        dfs( currentSum + numArray[depth], depth+1);
        dfs( currentSum - numArray[depth], depth+1);
    }
}