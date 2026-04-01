import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int n = 0, k = 0;

    public static void main(String[] args) throws Exception {
        String[] times = br.readLine().split(":");
        int hour = Integer.parseInt(times[0]);
        int minute = Integer.parseInt(times[1]);
        int second = Integer.parseInt(times[2]);

        String[] times2 = br.readLine().split(":");
        int hour2 = Integer.parseInt(times2[0]);
        int minute2 = Integer.parseInt(times2[1]);
        int second2 = Integer.parseInt(times2[2]);

        if(hour == hour2 && minute == minute2 && second == second2) {
            System.out.println("24:00:00");
            return;
        }

        if (second > second2) {
            second2 += 60;
            minute2 -= 1;
        }

        if (minute > minute2) {
            minute2 += 60;
            hour2 -= 1;
        }

        if (hour > hour2) {
            hour2 += 24;
        }

        int time2 = (hour2 * 60 * 60) + (minute2 * 60) + second2;
        int time1 = (hour * 60 * 60) + (minute * 60) + second;
        int diff = time2 - time1;

        System.out.printf("%02d:%02d:%02d%n", (diff / 3600), (diff % 3600) / 60, diff % 60);


    }


}