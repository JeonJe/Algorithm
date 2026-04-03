import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int n = 0, m = 0;
    static boolean[] visited;

    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        int[] arr = new int[m];
        visited = new boolean[n+1];


        dfs(0, arr);


    }

    static void dfs(int idx, int[] arr) {
        if (idx == m) {
            for(int i : arr) {
                System.out.print(i + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 0; i < n; i++) {
            if (visited[i + 1]) continue;
            
            arr[idx] = i + 1;
            visited[i + 1] = true;
            dfs(idx + 1, arr);
            visited[i + 1] = false;
        }

    }


}