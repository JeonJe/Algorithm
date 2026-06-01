class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n <= 0) {
            return false;
        }

        int cal = n & (n - 1);
        if(cal == 0) {
            return true;
        } 
        return false;
    }
}