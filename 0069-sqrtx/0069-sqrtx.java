class Solution {
    public int mySqrt(int x) {
        if (x < 2) {
            return x;
        }

        int left = 1;
        int right  =  (int) Math.floor( x / 2);

        while(left <= right) {
            int mid = (int) Math.floor((left + ((right-left) / 2)));

             long squre = (long) mid * mid;

            if(squre == x) {
                return  mid;
            } else if(squre < x) {
                left =  mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return right;
       
    }


}