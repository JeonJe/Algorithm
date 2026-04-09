import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int n = 0, m = 0;
    static boolean[] visited;

    public static void main(String[] args) throws Exception {
        String input = br.readLine();

        String[] digitalHumanities = new String[4];
        digitalHumanities[0] = "social";
        digitalHumanities[1] = "history";
        digitalHumanities[2] = "language";
        digitalHumanities[3] = "literacy";

        String[]  publicBigdata = new String[3];
        publicBigdata[0] = "bigdata";
        publicBigdata[1] = "public";
        publicBigdata[2] = "society";

        for (String digitalHumanity : digitalHumanities) {
            if(input.contains(digitalHumanity)) {
                System.out.println("digital humanities");
                return;
            }
        }

        for (String publicBigdata1 : publicBigdata) {
            if(input.contains(publicBigdata1)) {
                System.out.println("public bigdata");
                return;
            }
        }



    }
}