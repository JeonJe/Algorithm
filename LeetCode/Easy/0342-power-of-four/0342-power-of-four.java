class Solution {
    public boolean isPowerOfFour(int n) {
        if(n == 1) {
            return true;
        }
        if(n <= 0) {
            return false;
        }

        while(n > 1) {
            int r = n % 4;
            if(r != 0) {
                return false;
            } 
            n = n / 4;
        }
        return true;
    }
}