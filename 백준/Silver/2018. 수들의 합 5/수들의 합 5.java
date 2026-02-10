
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        //System.setIn(new FileInputStream("input.txt"));  // 제출 시 이 줄만 주석처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int result = 0;
        for (int i = n; i > 0; i--) {
            int sum = i;
            int cur = i;
            while (sum < n) {
                cur--;
                sum += cur;
            }

            if (n == sum) {
                result++;
            }
        }
        System.out.println(result);
    }


}
