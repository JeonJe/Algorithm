import java.util.*;
import java.io.*;

class Solution {
    
    private List<String> answer =new ArrayList<>();
    public String[] solution(String[][] tickets) {
                
        boolean[] visited = new boolean[tickets.length];        
        List<String> path = new ArrayList<String>();
        
        path.add("ICN");        
        dfs("ICN", tickets, visited, path, 0);

        Collections.sort(answer);
        
        return answer.get(0).split(" ");
    }
    
    private void dfs(String current, String[][] tickets, boolean[] visited, List<String> path, int depth) {

        if(depth >= tickets.length) {               
            answer.add(String.join(" ", path.toArray(new String[0])));
            return ;
        }
        
        for (int i = 0 ; i < tickets.length; i++) {
            if(tickets[i][0].equals(current) && !visited[i]) {
                visited[i] = true;
                path.add(tickets[i][1]);
                dfs(tickets[i][1], tickets, visited, path, depth+1);
                path.remove(path.size()-1);
                visited[i] = false;
             
            }
        }
     
     
        
        
        return ;
    }
}