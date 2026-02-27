import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] cycle = new int[n];
        int[] plan = new int[m];


        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            cycle[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            plan[i] = Integer.parseInt(st.nextToken());
        }

        boolean[] tangled = new boolean[n];
        int[] lastBrushedDay = new int[n];
        boolean[] isBrushYesterday = new boolean[n];

        for (int day = 1; day <= m; day++) {
            //각 강아지 털 엉침 체크
            for (int i = 0; i < n; i++) {
                //털이 엉키지 않은 상태에서 현재 날짜 - 마지막 날짜가 > 사이클 보다 크면
                if (!tangled[i] && day - lastBrushedDay[i] > cycle[i]) {
                    tangled[i] = true;
                }
            }

            //오늘 빗질
            int targetDogIndex = plan[day - 1] - 1;
            lastBrushedDay[targetDogIndex] = day;
            //2일 연속 털 빗었으면 엉킨 털이 풀림
            if (isBrushYesterday[targetDogIndex]) {
                tangled[targetDogIndex] = false;
            }

            for (int i = 0; i < n; i++) {
                if (i == targetDogIndex) {
                    isBrushYesterday[i] = true;
                } else {
                    isBrushYesterday[i] = false;
                }
            }
        }

        //M일에 털 빗기 후
        for (int i = 0; i < n; i++) {
            if (!tangled[i] && (m + 1) - lastBrushedDay[i] > cycle[i]) {
                tangled[i] = true;
            }
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            if (tangled[i]) {
                count++;
            }
        }
        System.out.println(count);
    }
}
