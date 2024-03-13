class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 0;
        int right = (int) Math.pow(10, 9);

        while(left+1 < right){
            int mid = left + ((right - left) / 2);

            if(check(mid,piles,h)) {
                right = mid;
            } else {
                left = mid;
            }
        }
        return right;
    }
     private boolean check(int mid, int[] piles, int h) {
        long spendHour = 0;
        for (int pile : piles) {
            int q = Math.floorDiv(pile, mid);
            int r = Math.floorMod(pile, mid);

            if(r > 0) {
                q++;
            }
            spendHour += q;
        }
       return spendHour <= (long) h;
    }
}