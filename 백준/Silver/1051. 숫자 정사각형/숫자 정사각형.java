

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {

    static int[][] arr;
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        n = Integer.parseInt(tokenizer.nextToken());
        m = Integer.parseInt(tokenizer.nextToken());

        if (n == 1 || m == 1) {
            System.out.println(1);
            return;
        }

        arr = new int[n][m];
        for (int i = 0; i < n; i++) {
            String row = reader.readLine();
            for (int j = 0; j < row.length(); j++) {
                arr[i][j] = Character.getNumericValue(row.charAt(j));
            }
        }

        int result = 0;
        int minDistance = Math.min(n, m);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int k = 0; k < minDistance; k++) {
                    if ((isSame(i, j, k))) {
                        result = Math.max(result, (k + 1) * (k + 1));
                    }
                }
            }
        }
        System.out.println(result);

    }

    private static boolean isSame(int i, int j, int k) {
        if (i + k >= n || j + k >= m) {
            return false;
        }
        if (arr[i][j] != arr[i + k][j]) {
            return false;
        }
        if (arr[i][j] != arr[i][j + k]) {
            return false;
        }
        if (arr[i][j] != arr[i + k][j + k]) {
            return false;
        }
        return true;
    }
}



