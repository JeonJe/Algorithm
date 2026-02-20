import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[] arr;
    static boolean[] visited;
    static int[] temp;
    static int res =0;

    static void dfs(int depth) {
        int cal = 0;
        if (depth == n) {
            for (int i = 1; i < n ; i++) {
                cal += Math.abs((temp[i - 1] - temp[i]));
            }
            res = Math.max(res, cal);
        } else {
            for (int i = 0; i < n; i++) {
                if (visited[i]){
                    continue;
                }else{
                    visited[i] = true;
                    temp[depth] = arr[i];
                    dfs(depth + 1);
                    visited[i] = false;

                }

            }

        }


    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        visited = new boolean[n];
        temp = new int[n];

        Arrays.fill(arr, 0);
        Arrays.fill(temp, 0);
        Arrays.fill(visited, false);

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        dfs(0);


        System.out.println("res = " + res);
    }
}