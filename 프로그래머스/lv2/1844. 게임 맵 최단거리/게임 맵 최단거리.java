import java.util.*;
import java.io.*;

class Solution {
    private int[] dx = {1,0,-1,0};
    private int[] dy = {0,1,0,-1};
    
    public int solution(int[][] maps) {
        int answer = 0;
        int height = maps.length;
        int width = maps[0].length;
        
        answer = bfs(maps, height, width);
        return answer;
    }
    
    private int bfs(int[][] maps, int height, int width) {
        boolean[][] visited = new boolean[height][width];
        visited[0][0] = true;
        
        Queue<int[]> que = new LinkedList<int[]>();
        que.offer(new int[]{0,0,1});
        
        while(!que.isEmpty()){
            int[] cur = que.poll();
            int cx = cur[0], cy = cur[1], cdist = cur[2];
            
            if (cx == height-1 && cy == width-1) {
                return cdist;
            }
            
            for (int i = 0 ; i < dx.length; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                
                if (0 <= nx && nx < height && 0 <= ny && ny < width) {
                    if (!visited[nx][ny] && maps[nx][ny] != 0) {
                        visited[nx][ny] = true;
                        que.offer(new int[]{nx, ny, cdist+1});
                    }
                }
            }
            
        }
        
        return -1;
    }
    
}