import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int N;
    private static int M;

    public static void main(String[] args) throws Exception {
        //System.setIn(new FileInputStream("input.txt"));  // 제출 시 이 줄만 주석처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        //선택한 숫자들 표시
        boolean[] visited = new boolean[N];

        //현재 선택한 숫자 순서
        List<Integer> temp = new ArrayList<>();

        dfs(visited, temp, 0);


    }

    private static void dfs(boolean[] visited, List<Integer> temp, int count) {
        if (count == M) {
            print(temp);
            return;
        }

        for (int i = 0; i < N; i++) {
            if (visited[i]) {
                continue;
            }
            //숫자 선택
            visited[i] = true;
            temp.add(i);

            dfs(visited, temp, count + 1);

            visited[i] = false;
            temp.remove(temp.size() - 1);
        }

    }

    private static void print(List<Integer> temp) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < temp.size() - 1; i++) {
            sb.append(temp.get(i) + 1 + " ");
        }
        sb.append(temp.get(temp.size() - 1) + 1).append("\n");

        System.out.print(sb.toString());

    }
}
