class Solution {
    public String largestGoodInteger(String num) {

        for (int i = 9; i >= 0; i--) {
            String current = String.valueOf(i) + String.valueOf(i) + String.valueOf(i);
            if (num.contains(current)) {
                return current;
            }
        }
        return "";

    }
}