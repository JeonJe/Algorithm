import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int n = 0, k = 0;

    public static void main(String[] args) throws Exception {
        n = Integer.parseInt(br.readLine());

        int cnt = 1;

        while (true) {
            n -= cnt;
            if (n <= 0) {
                break;
            }
            cnt++;
        }

        if (cnt % 2 == 0 && n == 0) {
            //친구에서 모든 돌을 다 가져간 경우
            cnt++;
            System.out.println(cnt);
        } else if (cnt % 2 == 0) {
            //친구가 진 경우
            System.out.println("0");

        } else {
            //푸앙이가 이기기 위해 돌 추가
            System.out.println(Math.abs(n));
        }


    }


}