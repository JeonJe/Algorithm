
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    static int n;
    static int m;
    static int[][] graph;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        n = Integer.parseInt(tokenizer.nextToken());
        m = Integer.parseInt(tokenizer.nextToken());

        graph = new int[n + 1][n + 1];
        visited = new boolean[n + 1];

        for (int i = 0; i < m; i++) {
            StringTokenizer inputs = new StringTokenizer(reader.readLine());
            int start = Integer.parseInt(inputs.nextToken());
            int end = Integer.parseInt(inputs.nextToken());

            graph[start][end] = 1;
            graph[end][start] = 1;

        }
        int count = 0;
        for (int i = 1; i < n + 1; i++) {
            if (!visited[i]) {
                count++;
                dfs(i, visited);
            }
        }
        System.out.println(count);
    }

    private static void dfs(int start, boolean[] visited) {
        visited[start] = true;

        for (int adj = 1; adj < n + 1; adj++) {
            if (graph[start][adj] == 1 && !visited[adj]) {
                dfs(adj, visited);
            }
        }
    }

}


