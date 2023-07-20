import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        Arrays.sort(people);
        int left = 0, right = people.length-1;
        
        while(left <= right) {
            if(left==right){
                answer++;
                right--;
                continue;
            }
            if (people[left] + people[right] <= limit) {
                left++;
                right--;
                answer++;
            } else{
                // 제일 가벼운 사람과 같이 탈수 없는 무거운 사람은 혼자 태워보낸다.
                right--;
                answer++;
            }
            
        }
        
        
        return answer;
    }
}