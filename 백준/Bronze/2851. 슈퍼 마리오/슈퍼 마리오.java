import java.io.BufferedReader;
//import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        //System.setIn(new FileInputStream("input.txt"));  // 제출 시 이 줄만 주석처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int sum = 0;
        int answer = 0;

        for (int i = 0; i < 10; i++) {
            sum += Integer.parseInt(br.readLine());
            if (Math.abs(100 - sum) < Math.abs(100 - answer) || (sum >= 100 && Math.abs(100 - sum) == Math.abs(100 - answer))) {
                answer = sum;
            }

        }
        System.out.println(answer);


    }


}
