import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        Stack<Character> stack = new Stack<>();
        char[] chars = s.toCharArray();
        
        for (int i = 0; i < chars.length; i++){
            if (chars[i] == '(') {
                stack.push('(');
            } else{
                if (stack.size() <= 0  || stack.peek() == ')'){
                    return false;
                }
                stack.pop();
            }
        }
        return stack.size() > 0 ? false : true;

    }
}