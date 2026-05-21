class Solution {
    public int mySqrt(int x) {
        if (x < 2) {
            return x;
        }

        int left = 1;
        int right  =  (int) Math.floor( x / 2);

        while(left <= right) {
            long mid = (long) Math.floor((left + right) / 2);

            long squre = mid * mid;

            if(squre == x) {
                return (int) mid;
            } else if(squre < x) {
                left = (int)mid + 1;
            } else {
                right = (int) mid - 1;
            }
        }

        return right;
       
    }


}