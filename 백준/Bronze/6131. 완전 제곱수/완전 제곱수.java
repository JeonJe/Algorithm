import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        //System.setIn(new FileInputStream("input.txt"));  // 제출 시 이 줄만 주석처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        double epsilon = 1e-9;
        int result = 0;

        for (int b = 1; b <= 500; b++) {
            double a = Math.sqrt(b * b + n);
            boolean isInteger = Math.abs(a - Math.round(a)) < epsilon;
            if (a <= 500 && isInteger) {
                result++;
            }
        }
        System.out.println(result);

    }
}
