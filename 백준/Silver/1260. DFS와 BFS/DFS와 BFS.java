import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        //System.setIn(new FileInputStream("input.txt"));  // 제출 시 이 줄만 주석처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());

        List<Integer>[] graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());

            graph[from].add(to);
            graph[to].add(from);
        }
        for (int i = 1; i <= n; i++) {
            Collections.sort(graph[i]);
        }

        //dfs
        List<Integer> temp = new ArrayList<>();
        boolean[] visited = new boolean[n + 1];
        visited[v] = true;
        dfs(v, graph, temp, visited);
        System.out.println(sb.substring(0, sb.length() - 1));

        //bfs
        sb.setLength(0);
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        deque.offer(v);
        Arrays.fill(visited, false);
        visited[v] = true;


        while (!deque.isEmpty()) {
            int cur = deque.poll();
            sb.append(cur).append(" ");

            for (int adj : graph[cur]) {
                if (visited[adj]) {
                    continue;
                }
                visited[adj] = true;
                deque.offer(adj);
            }
        }
        System.out.println(sb.substring(0, sb.length() - 1));
    }

    private static void dfs(int v, List<Integer>[] graph, List<Integer> temp, boolean[] visited) {
        sb.append(v).append(" ");

        for (Integer adj : graph[v]) {
            if (visited[adj]) {
                continue;
            }
            visited[adj] = true;
            temp.add(adj);
            dfs(adj, graph, temp, visited);
            temp.remove(temp.size() - 1);
        }

    }
}
