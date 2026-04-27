class Solution {
    //상,우,하,좌
    private static int[][] directions = {{-1,0}, {0,1},{1,0},{0,-1}};

    //상,우,하,좌
    private static boolean[][] streets = {
        {false,true,false,true},
        {true,false,true,false},
        {false,false,true,true},
        {false,true,true,false},
        {true,false,false,true},
        {true,true,false,false}
    };

    private static boolean[][] visited;

    private static int m;
    private static int n;
    private static boolean answer;

    

    public boolean hasValidPath(int[][] grid) {
        m = grid.length;
        n = grid[0].length;

        visited = new boolean[m][n];

        answer = false;
        dfs(0,0,grid);

        return answer;

    }

    private static void dfs(int x, int y, int[][] grid) {
        if(x == m-1 && y == n-1) {
            answer = true;
        }

        visited[x][y] = true;

        for(int i = 0; i < 4; i++) {
            int nx = x + directions[i][0];
            int ny = y + directions[i][1];

            if(nx < 0 || nx >= m || ny < 0 || ny >=n) {
                continue;
            }
            if(visited[nx][ny]) {
                continue;
            }

            //현재 셀이 다음셀과 연결 
            boolean[] currentToNext = streets[grid[x][y]-1];
            if(!currentToNext[i]){
                continue;
            }

            //다음 셀이 현재셀과 연결 
            boolean[] nextToCurrent = streets[grid[nx][ny]-1];
            if(!nextToCurrent[(i + 2) % 4]) {
                continue;
            }
            dfs(nx,ny,grid);
        }
    }
}