class Solution {
    public int findClosest(int x, int y, int z) {
        int position1 = Math.abs(x - z);
        int position2 = Math.abs(y - z);

        if(position1 == position2) {
            return 0;
        }
        return position1 < position2 ? 1 : 2; 
        
    }
}