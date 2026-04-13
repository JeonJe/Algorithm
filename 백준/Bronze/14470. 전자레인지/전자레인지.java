import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int n = 0, m = 0;
    static boolean[] visited;

    static List<Character> vowels = List.of('a', 'e', 'i', 'o', 'u');
    public static void main(String[] args) throws Exception {
        //현재 온도
        int a = Integer.parseInt(br.readLine());

        boolean isFrozen = a < 0;
        //목표 온도
        int b = Integer.parseInt(br.readLine());

        //얼어있는 고기 1도 데우는데 걸리는 시간
        int c = Integer.parseInt(br.readLine());

        //얼어있는 고기 해동하는데 걸리는 시간 d
        int d = Integer.parseInt(br.readLine());
        //얼어있지 ㅇ낳는 고기 1도 데우는데 걸리는 시간
        int e = Integer.parseInt(br.readLine());

        int cnt = 0;


        while(a < b) {

            //고기가 얼어 있고 온도가 0℃ 미만일 때 : 온도가 C초에 1℃씩 오른다.
            if(isFrozen && a < 0) {
                a += 1;
                cnt += c;
            } else if (isFrozen && a == 0) {
                //고기가 얼어 있고 온도가 정확히 0℃일 때 : 얼어 있지 않은 상태로 만드는(해동하는) 데 D초가 걸린다.
                isFrozen = false;
                cnt += d;
            } else if (!isFrozen) {
                //고기가 얼어 있지 않을 때 : 온도가 E초에 1℃씩 오른다.
                a += 1;
                cnt += e;

            }
        }
        System.out.println(cnt);

    }

}