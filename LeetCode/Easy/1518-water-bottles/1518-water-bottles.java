class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int answer = 0;
        int emptyBottles = 0;

        // 마실 물이 있거나, 빈병으로 교환할 수 있을 동안 반복
        while (numBottles > 0) {
            // 1) 물 마시기
            answer += numBottles;
            emptyBottles += numBottles;

            // 2) 교환 가능한지 확인
            if (emptyBottles < numExchange) break;

            // 3) 교환
            numBottles = emptyBottles / numExchange;
            emptyBottles = emptyBottles % numExchange;
        }

        return answer;
    }
}