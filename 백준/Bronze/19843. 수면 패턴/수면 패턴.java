import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int n = 0, k = 0;

    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());


        Map<String, Integer> map = new HashMap<>();
        map.put("Mon", 0);
        map.put("Tue", 1);
        map.put("Wed", 2);
        map.put("Thu", 3);
        map.put("Fri", 4);
        map.put("Sat", 5);
        map.put("Sun", 6);

        int weekdaySum = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String startDay = st.nextToken();
            int startHour = Integer.parseInt(st.nextToken());
            String endDay = st.nextToken();
            int endHour = Integer.parseInt(st.nextToken());

            int start = map.get(startDay) * 24 + startHour;
            int end = map.get(endDay) * 24 + endHour;
            weekdaySum += (end - start);
        }

        if (weekdaySum > t) {
            System.out.println("0");
            return;
        }

        if (t - weekdaySum > 48) {
            System.out.println("-1");
            return;
        }

        System.out.println(t - weekdaySum);


    }


}