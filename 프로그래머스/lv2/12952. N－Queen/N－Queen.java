class Solution {
    int[] rows;
    public int solution(int n) {
        
        int answer = 0;
        rows = new int[n];
        answer = dfs(0,n);
        
        return answer;
    }
    
    public int dfs(int depth,int n){
        if (depth == n){
            return 1;
        }
        int cnt = 0;
        for (int i = 0; i < n; i++){
            rows[depth] = i;
            if (isValid(depth)){
                cnt += dfs(depth + 1, n);
            }
        }
        return cnt;
        
    }
    
    public boolean isValid(int x){
        
        for (int i = 0; i < x; i++){
            if(rows[x] == rows[i] || (Math.abs(x-i) == Math.abs(rows[x]-rows[i]))){
                return false;
            }
        }
        return true;
    }
    
}