import java.util.*;
import java.io.*;

class Solution {
    private boolean[] visited;
    public int solution(int n, int[][] computers) throws Exception{
        int answer = 0;
        visited = new boolean[computers.length];
        
        for(int i = 0; i < computers.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(computers, i);
                answer++;
            }    
        }
        return answer;
    }
    
    private void dfs(int[][] computers, int start) {

            for (int i = 0; i < computers[start].length; i++) {
                if (computers[start][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    dfs(computers, i);
                }
            }    
        
    }
}