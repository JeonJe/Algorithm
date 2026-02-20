import java.io.BufferedReader;
import java.io.FileReader;
import java.util.StringTokenizer;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken()) - 1; //index
        int r = Integer.parseInt(st.nextToken()) - 1; //index

        int[] nums = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }


        int prev = l - 1;
        int cur = l;
        while (prev >= 0) {
            if (nums[prev] > nums[cur]) {
                System.out.println("0");
                System.exit(0);
            }
            prev--;
            cur--;
        }

        cur = r;
        int next = r + 1;
        while (next < n) {
            if (nums[cur] > nums[next]) {
                System.out.println("0");
                System.exit(0);
            }
            cur++;
            next++;
        }

        System.out.println("1");

    }

}