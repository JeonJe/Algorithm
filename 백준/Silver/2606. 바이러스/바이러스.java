
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {

    static int result = 0;
    static int[][] graph;
    static boolean[] visited;
    static int computerCount;
    static int nodeCount;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        computerCount = Integer.parseInt(reader.readLine());
        nodeCount = Integer.parseInt(reader.readLine());

        graph = new int[computerCount + 1][computerCount + 1];
        visited = new boolean[computerCount + 1];

        for (int i = 0; i < nodeCount; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(reader.readLine());
            int start = Integer.parseInt(stringTokenizer.nextToken());
            int end = Integer.parseInt(stringTokenizer.nextToken());

            graph[start][end] = 1;
            graph[end][start] = 1;
        }
        dfs(1);
        System.out.println(result);
    }

    private static void dfs(int current) {
        visited[current] = true;

        for (int adj = 0; adj < computerCount + 1; adj++) {
            if (graph[current][adj] == 1 && !visited[adj]) {
                visited[adj] = true;
                result++;
                dfs(adj);
            }
        }
    }
}


