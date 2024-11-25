
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(reader.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            int cnt = 0;
            int circleNumber = Integer.parseInt(reader.readLine());
            for (int j = 0; j < circleNumber; j++) {
                st = new StringTokenizer(reader.readLine());
                int cx = Integer.parseInt(st.nextToken());
                int cy = Integer.parseInt(st.nextToken());
                int r = Integer.parseInt(st.nextToken());

                boolean inCircle1 = isInCircle(cx, cy, r, x1, y1);
                boolean inCircle2 = isInCircle(cx, cy, r, x2, y2);
                if (inCircle1 && inCircle2) {
                    continue;
                }
                if (inCircle1) {
                    cnt++;
                }
                if (inCircle2) {
                    cnt++;
                }
                sb.append(cnt).append("\n");
            }
            System.out.println(cnt);

        }
    }

    private static boolean isInCircle(int cx, int cy, int r, int x, int y) {
        return Math.pow(cx - x, 2) + Math.pow(cy - y, 2) < Math.pow(r, 2);
    }
}


