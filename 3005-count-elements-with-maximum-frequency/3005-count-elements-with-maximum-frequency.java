class Solution {
    public int maxFrequencyElements(int[] nums) {
        int[] arr = new int[101];

        int maxFrequency = 0;
        for(int n : nums) {
            arr[n] += 1;
            maxFrequency = Math.max(maxFrequency, arr[n]);
        }

        int answer = 0;
        for(int i = 1; i <= 100; i++) {
            if(arr[i] == maxFrequency ) {
                answer += arr[i];
            }
        }
        return answer;
        
    }
}