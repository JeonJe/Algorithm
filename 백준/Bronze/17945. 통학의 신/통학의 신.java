import java.util.*;
import java.io.*;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
//        System.setIn(new FileInputStream("input.txt"));  // 제출 시 이 줄만 주석처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        for (int x = -1000; x <= 1000; x++) {
            int target = (x * x) + (2 * a * x) + b;
            if (target == 0) {
                System.out.print(x + " ");
            }
        }

    }
}
