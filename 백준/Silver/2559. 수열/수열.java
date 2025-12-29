import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] nums = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) nums[i] = Integer.parseInt(st.nextToken());


        int slidingWindow = 0;
        for (int i = 0; i <= K - 1; i++) {
            slidingWindow += nums[i];
        }
        int answer = slidingWindow;

        // right가 배열 밖으로 튀어나가지 않을 동안
        // 현재 left가 가리키고 있는 값을 윈도우에서 뺴고, left증가
        // right를 증가시키고, 현재 right가 가리키고 있는 값을 더함
        for (int i = K; i < N; i++) {
            slidingWindow += nums[i];
            slidingWindow -= nums[i - K];
            answer = Math.max(answer, slidingWindow);
        }

        System.out.println(answer);
    }
}
