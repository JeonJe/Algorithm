class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i = 1; i <= n; i++){
            int sum = 0;
            int start_value = i;
            
            while (sum < n){
                sum += start_value;
                start_value++;
            }
            
            if(sum == n){
                System.out.println(i);
                answer++;
            }
            
        }
        return answer;
    }
}