class Solution {
    private static int[] dx = {1,0,-1,0};
    private static int[] dy = {0,1,0,-1};
    private static boolean[][] visited;
    private int n;
    private int m;
    public int numIslands(char[][] grid) {
        n = grid.length;
        m = grid[0].length;

        visited = new boolean[n][m];

        int answer = 0;

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(!visited[i][j] && grid[i][j] == '1') {
                    answer++;
                    bfs(i,j,grid);
                }
            }
        }
        return answer;
    }

    private void bfs(int x, int y, char[][] grid) {
        visited[x][y] = true;
        Deque<int[]> deque = new ArrayDeque<>();
        deque.offer(new int[]{x,y});

        while(!deque.isEmpty()) {
            int[] current = deque.poll();
            int cx = current[0];
            int cy = current[1];

            for(int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if(0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if(!visited[nx][ny] && grid[nx][ny] == '1') {
                        visited[nx][ny] = true;
                        deque.offer(new int[]{nx,ny});
                    }
                }
            }
        }
    }


}