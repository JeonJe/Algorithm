import java.util.*;
import java.io.*;

class Solution
{
    public int solution(String s)
    {
        int answer = -1;
        Stack<Character> st = new Stack<>();
        for (char ch : s.toCharArray()){
            if (st.empty() || st.peek() != ch){
                st.push(ch);
            } else {
                st.pop();
            }
        }
        
        return st.size() == 0 ? 1 : 0;
    }
}