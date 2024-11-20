

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

class Main {

    static int n, m, y;
    static int[][] graph;
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(reader.readLine());
        n = Integer.parseInt(stringTokenizer.nextToken());
        m = Integer.parseInt(stringTokenizer.nextToken());
        y = Integer.parseInt(stringTokenizer.nextToken());

        graph = new int[n + 1][n + 1];

        for (int i = 0; i < m; i++) {
            stringTokenizer = new StringTokenizer(reader.readLine());
            int start = Integer.parseInt(stringTokenizer.nextToken());
            int end = Integer.parseInt(stringTokenizer.nextToken());

            graph[start][end] = 1;
            graph[end][start] = 1;
        }

        visited = new boolean[n + 1];

        dfs(y);
        System.out.println(sb.toString());
        initVariables();

        bfs(y);
        System.out.println(sb.toString());
    }

    private static void dfs(int start) {
        visited[start] = true;
        sb.append(start + " ");

        for (int i = 0; i < n + 1; i++) {
            if (graph[start][i] == 1 && !visited[i]) {
                dfs(i);
            }
        }
    }

    private static void bfs(int start) {
        Deque<Integer> que = new ArrayDeque<>();
        visited[start] = true;
        que.offer(start);
        sb.append(start + " ");

        while (!que.isEmpty()) {
            Integer current = que.poll();

            for (int adj = 0; adj < n + 1; adj++) {
                if (graph[current][adj] == 1 && !visited[adj]) {
                    que.offer(adj);
                    visited[adj] = true;
                    sb.append(adj + " ");
                }
            }
        }
    }

    private static void initVariables() {
        Arrays.fill(visited, false);
        sb.setLength(0);
    }
}


