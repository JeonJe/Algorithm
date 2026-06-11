class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {

        List<Boolean> answer = new ArrayList<>();
        //제일 큰 값 찾기 
        int greatest = 0;
        for(int c : candies) {
            if(c > greatest) {
                greatest = c;
            }
        }

        for(int c : candies) {
            int s = c + extraCandies;
            if (s >= greatest) {
                answer.add(true);
            } else {
                answer.add(false);
            }
        }

        return answer;
        
    }
}