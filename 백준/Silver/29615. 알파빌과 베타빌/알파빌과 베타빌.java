import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] orders = new int[n];
        Set<Integer> friends = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            orders[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            friends.add(Integer.parseInt(st.nextToken()));
        }

        //orders 에서 m명 중 쫓아 낼 사람 수
        int outCount = 0;
        for(int i = 0; i < m; i++) {
            if(!friends.contains(orders[i])) {
                outCount++;
            }
        }

        System.out.println(outCount);

        br.close();
    }
}