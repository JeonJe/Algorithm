import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String[] arr = new String[numbers.length];
        
        for (int i=0; i < arr.length; i++){
            arr[i] = Integer.toString(numbers[i]);
        }
        
        Arrays.sort(arr, (a,b) -> (b+a).compareTo(a+b));
        
        if (arr[0].equals("0")){
            return "0";
        }
        
        StringBuilder answer = new StringBuilder();
        for (int i=0; i<arr.length; i++){
            answer.append(arr[i]);
        }
        return answer.toString();
        
    }
}