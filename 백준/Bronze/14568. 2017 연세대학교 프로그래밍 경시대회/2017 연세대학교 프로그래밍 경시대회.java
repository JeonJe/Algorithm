import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int answer = 0;

    public static void main(String[] args) throws Exception {
        //System.setIn(new FileInputStream("input.txt"));  // 제출 시 이 줄만 주석처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());


        //남규
        for (int i = 1; i < n; i++) {
            //영휸
            for (int j = 1; j < n; j++) {
                //택희
                for (int k = 1; k < n; k++) {
                    if (i + j + k == n) {
                        if (i >= j + 2) {
                            if (k % 2 == 0) {
                                answer++;
                            }
                        }
                    }
                }
            }
        }


        System.out.println(answer);
    }


}
