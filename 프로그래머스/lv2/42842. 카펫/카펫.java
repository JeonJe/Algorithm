import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        int totalArea = brown + yellow;
        
        for (int i = 1 ; i < totalArea; i++) {
            int brownX = i;
            int brownY = 0;
            
            if (totalArea % brownX == 0) {
                brownY = totalArea / brownX;
            } else {
                continue;
            }
            
            if(brownX < brownY) {
                continue;
            }
            
            int yellowX = brownX - 2;
            int yellowY = brownY - 2;
            
            if (yellowX*yellowY == yellow){
               answer[0] = brownX;
               answer[1] = brownY;
               break;
            }
        }
        
        
        return answer;
    }
}