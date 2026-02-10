import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        //System.setIn(new FileInputStream("input.txt"));  // 제출 시 이 줄만 주석처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int left = 1, right = 1;
        int sum = 1;
        int count = 0;
        while (left <= n && right <= n) {
            if (sum == n) {
                count++;
                sum -= left;
                left++;
            } else if (sum < n) {
                right++;
                sum += right;
            } else {
                sum -= left;
                left++;
            }
        }

        System.out.println(count);


    }


}
