import java.util.*;

class Solution {
    public int solution(int[][] info, int n, int m) {
        final int INF = 1_000_000_000;
        int answer = INF;
        int itemCount = info.length;
        
        // dp[i][j] = i번째 물건까지 훔쳤을 때, B 도둑이 흔적 j개를 남겼다면, A 도둑이 남긴 흔적 최소 합
        //itemCount + 1 -> 물건을 안훔친 0도 포함
        //m은 B가 남길수 있는 흔적의 개수 0부터 m-1
        int[][] dp = new int[itemCount+1][m];
        
        for(int i = 0; i <= itemCount; i++) {
            Arrays.fill(dp[i], INF);
        }
        
        dp[0][0] = 0;
        
        for(int i = 1; i <= itemCount; i++) {
            int a = info[i-1][0];
            int b = info[i-1][1];
            
            for(int j = 0; j < m; j++) {
                if(dp[i-1][j] == INF) {
                    continue;
                }
                
                //i번째 물건을 A가 훔칠 때, B흔적은 j로 유지되고, A는 a만큼 증가
                int aSum = dp[i-1][j] + a;
                if(aSum < n) {
                    dp[i][j] = Math.min(dp[i][j], aSum);
                }
                
                //i번재 물건을 B가 훔칠 때, A는 유지되고, B흔적은 j+b로 증가
                int j2 = j+b;
                if(j2 < m) {
                    dp[i][j2] = Math.min(dp[i][j2], dp[i-1][j]);
                }
                
            }
            
        }
        for(int j = 0; j < m; j++) {
            answer = Math.min(answer, dp[itemCount][j]);
        }
        
        return answer == INF ? -1 : answer ;
    }
}