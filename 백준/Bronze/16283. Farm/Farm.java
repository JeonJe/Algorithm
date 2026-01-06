import java.util.*;
import java.io.*;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
//        System.setIn(new FileInputStream("input.txt"));  // 제출 시 이 줄만 주석처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        // 양 한마리가 먹는 사료 a그램
        int a = Integer.parseInt(st.nextToken());
        // 염소 한마리가 먹는 사료 b그램
        int b = Integer.parseInt(st.nextToken());
        // 전체 수
        int n = Integer.parseInt(st.nextToken());
        // 하루 소비량
        int w = Integer.parseInt(st.nextToken());

        int count = 0;
        int answerX = 0, answerY = 0;
        // 양의 수
        for (int x = 1; x <= 1000; x++) {
            int y = n - x;
            if (y >= 1 && w - a * x == b * y) {
                count++;
                answerX = x;
                answerY = y;
            }
        }

        if (count == 1) {
            System.out.printf("%d %d", answerX, answerY);
            return;
        }
        System.out.println(-1);


    }
}
