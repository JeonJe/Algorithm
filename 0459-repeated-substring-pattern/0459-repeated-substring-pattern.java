class Solution {
    public boolean repeatedSubstringPattern(String s) {
        
        for(int i = 0; i < s.length()-1; i++) {
            String cur = s.substring(0,i+1);

            if( (s + cur).equals(cur + s)) {    
                return true;
            }
        }
        return false;
    }
   
}