import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    static String[][] DIGITS = {
            {"000000", "001100", "010010", "010010", "010010", "001100", "000000" }, // 0
            {"000000", "000100", "001100", "000100", "000100", "000100", "000000" }, // 1
            {"000000", "011110", "000010", "011110", "010000", "011110", "000000" }, // 2
            {"000000", "011100", "000010", "000100", "000010", "011100", "000000" }, // 3
            {"000000", "000100", "001100", "010100", "111110", "000100", "000000" }, // 4
            {"000000", "011110", "010000", "011100", "000010", "010010", "001100" }, // 5
            {"000000", "010000", "010000", "011110", "010010", "011110", "000000" }, // 6
            {"000000", "011110", "000010", "000100", "000100", "000100", "000000" }, // 7
            {"000000", "011110", "010010", "011110", "010010", "011110", "000000" }, // 8
            {"011110", "010010", "010010", "011110", "000010", "000010", "000010" }, // 9
    };

    public static void main(String[] args) throws Exception {

        String[] rows = new String[7];
        for (int i = 0; i < 7; i++) {
            rows[i] = br.readLine();
        }

        // 전구 갯수
        int n = rows[0].length() / 6;
        List<Integer> original = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            original.add(readNumber(rows, i * 6));
        }

        int[] sorted = original.stream().mapToInt(Integer::intValue).sorted().toArray();
        boolean[] visited = new boolean[n];
        List<Integer> cur = new ArrayList<>();
        List<List<Integer>> all = new ArrayList<>();
        dfs(sorted, visited, cur, all);

        int idx = all.indexOf(original);

        if (idx == -1 || idx == all.size() - 1) {
            System.out.println("The End");
        } else {
            printBoard(all.get(idx + 1));
        }


    }

    private static void dfs(int[] perm, boolean[] visited, List<Integer> cur, List<List<Integer>> all) {
        if(cur.size() == perm.length) {
            all.add(new ArrayList<>(cur));
            return;
        }

        for(int i = 0; i < perm.length; i++) {
            if(visited[i]) continue;
            visited[i] = true;
            cur.add(perm[i]);
            dfs(perm, visited, cur, all);
            cur.remove(cur.size() - 1);
            visited[i] = false;
        }

    }

    private static void printBoard(List<Integer> nums) {
        for (int r = 0; r < 7; r++) {
            for (int num : nums) {
                sb.append(DIGITS[num][r]);
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }

    private static int readNumber(String[] rows, int col) {
        for (int digit = 0; digit <= 9; digit++) {
            boolean matched = true;
            for (int r = 0; r < 7; r++) {
                String chunk = rows[r].substring(col, col + 6);
                if (!chunk.equals(DIGITS[digit][r])) {
                    matched = false;
                }
            }
            if (matched) {
                return digit;
            }
        }
        return -1;
    }


}