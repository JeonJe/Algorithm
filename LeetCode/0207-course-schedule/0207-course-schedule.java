class Solution {
    boolean[] visited, traced;
    ArrayList<Integer>[] graph;
    boolean result = true;
    
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        visited = new boolean[numCourses];
        traced = new boolean[numCourses];
         graph = new ArrayList[numCourses];

        for (int i = 0 ; i < numCourses; i ++){
            graph[i] = new ArrayList<Integer>();
        }
        for (int[] prerequisite : prerequisites) {
            int start = prerequisite[0];
            int end = prerequisite[1];
            graph[start].add(end);
        }

        for (int i = 0; i < numCourses; i++) {//전체 강의 dfs 탐색
            dfs(i);
            if (!result) {//사이클 탐지 시
                break;
            }
        }

        return result;
    }
    private void dfs(int index){
        if(visited[index]) {
            if(traced[index]){
                result = false;
            }
            return;
        }
        visited[index] = true;
        traced[index] = true;

        for (int i = 0 ; i < graph[index].size(); i++){
            dfs(graph[index].get(i));
        }
        traced[index] = false;
    }
}