import java.io.*;
import java.util.*;

class Solution {
    public String solution(String s) {
    
        String[] splitedStr = s.split(" ");
        long min = Integer.parseInt(splitedStr[0]);
        long max = Integer.parseInt(splitedStr[0]);
        
        for (int i = 1; i < splitedStr.length; i++){
            int cur = Integer.parseInt(splitedStr[i]);
            min = Math.min(min, cur);
            max = Math.max(max, cur);
        }
        StringBuilder sb = new StringBuilder();
        sb.append(String.valueOf(min));
        sb.append(" ");
        sb.append(String.valueOf(max));
        
        return sb.toString();
    }
}