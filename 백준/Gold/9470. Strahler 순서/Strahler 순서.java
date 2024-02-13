
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static List<List<Integer>> graph;
    private static int[] inDegree;
    private static int[] numSameDegree;
    private static int[] order;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
            int K = Integer.parseInt(stringTokenizer.nextToken());
            int M = Integer.parseInt(stringTokenizer.nextToken());
            int P = Integer.parseInt(stringTokenizer.nextToken());
            graph = new ArrayList<>();
            for(int i = 0; i < M+1; i++){
                graph.add(new ArrayList<>());
            }
            inDegree = new int[M + 1];
            numSameDegree = new int[M + 1];
            order = new int[M + 1];

            for (int i = 0; i < P; i++) {
                stringTokenizer = new StringTokenizer(br.readLine());
                int from = Integer.parseInt(stringTokenizer.nextToken());
                int to = Integer.parseInt(stringTokenizer.nextToken());
                graph.get(from).add(to);
                inDegree[to] += 1;
            }

            int maxValue = topologySort(M);
            System.out.println((t + 1) + " " + maxValue);
        }

    }

    private static int topologySort(int m){
        Queue<Integer> queue = new LinkedList<>();
        int answer = 0;

        for (int i = 1; i <= m; i++) {
            if(inDegree[i] == 0) {
                queue.add(i);
                order[i] = 1;
                numSameDegree[i] = 1;
            }
        }
        while (!queue.isEmpty()) {
            int current = queue.poll();

            if(numSameDegree[current] >= 2){
                order[current]++;
            }
            answer = Math.max(answer, order[current]);

            for (int adj : graph.get(current)) {
                inDegree[adj]--;

                if(inDegree[adj] == 0) {
                    queue.add(adj);
                }

                if(order[current] == order[adj]) {
                    numSameDegree[adj]++;
                } else if(order[adj] < order[current]) {
                    order[adj] = order[current];
                    numSameDegree[adj] = 1;
                }
            }

        }
        return answer;
    }

}
