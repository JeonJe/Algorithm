class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int sum = 0;
        for(String operation : operations) {
            if(operation.contains("+")) {
                sum++;
            } else if(operation.contains("-")){
                sum--;
            }
        }
        return sum;
    }
}