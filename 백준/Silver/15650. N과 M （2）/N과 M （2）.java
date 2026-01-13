import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int N;
    private static int M;
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
//        System.setIn(new FileInputStream("input.txt"));  // 제출 시 이 줄만 주석처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());


        boolean[] checked = new boolean[N];
        int[] temp = new int[N];
        // 현재 인덱스, 현재 선택한 값, 현재 선택한 갯수
        dfs(0, checked, temp, 0);

        sb.deleteCharAt(sb.length() - 1);
        System.out.print(sb);

    }

    private static void dfs(int idx, boolean[] checked, int[] temp, int cnt) {
        if (cnt == M) {
            for (int i = 0; i < M - 1; i++) {
                sb.append(temp[i]).append(" ");
            }
            sb.append(temp[M - 1]).append("\n");

            return;
        }

        for (int i = idx; i < N; i++) {
            checked[i] = true;
            temp[cnt] = i + 1;
            dfs(i + 1, checked, temp, cnt + 1);
            checked[i] = false;
            temp[cnt] = 0;

        }

    }

}
