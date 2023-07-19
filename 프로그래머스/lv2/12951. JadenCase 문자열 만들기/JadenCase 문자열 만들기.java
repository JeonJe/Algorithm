import java.util.*;
import java.io.*;
class Solution {
    public String solution(String s) throws Exception {
        boolean isFirst = true;
        StringBuilder result = new StringBuilder();
        
        for (char ch : s.toCharArray()) {
            if (Character.isLetter(ch)){
                if (isFirst) {
                    ch = Character.toUpperCase(ch);
                    isFirst = false;
                } else{
                    ch = Character.toLowerCase(ch);
                }
            } else if (Character.isDigit(ch) ){
              if (isFirst) {
                  isFirst = false;
              }  
            } else if ( Character.toString(ch).equals(" ") ) {
                isFirst = true;
            } 
            result.append(ch);
        }
        return result.toString();
    }
}