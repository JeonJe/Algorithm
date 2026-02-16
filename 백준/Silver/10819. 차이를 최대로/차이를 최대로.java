import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int answer = 0;
    private static int[] arr;
    private static int[] current;
    private static boolean[] visited;

    public static void main(String[] args) throws Exception {
        //System.setIn(new FileInputStream("input.txt"));  // 제출 시 이 줄만 주석처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        arr = new int[n];
        current = new int[n];
        visited = new boolean[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }


        dfs(0);

        System.out.println(answer);
    }

    private static void dfs(int depth) {
        if (depth == arr.length) {
            //최대 값인지 확인
            int sum = 0;
            for (int i = 0; i < current.length - 1; i++) {
                sum += Math.abs(current[i] - current[i + 1]);
            }

            answer = Math.max(answer, sum);
            return;
        }


        for (int i = 0; i < arr.length; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            //depth 번째 수를 arr[i]로 선택
            current[depth] = arr[i];
            dfs(depth + 1);
            visited[i] = false;
        }
    }


}
