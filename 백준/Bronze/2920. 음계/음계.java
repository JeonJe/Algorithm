import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        Integer[] arr = new Integer[8];
        for (int i = 0; i < 8; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        boolean isAscending = true;
        boolean isDescending = true;

        for (int i = 0; i < 7; i++) {
            if (arr[i] < arr[i + 1]) {
                isDescending = false;
            }
            if (arr[i] > arr[i + 1]) {
                isAscending = false;
            }
        }

        if (isAscending) {
            System.out.println("ascending");
        } else if (isDescending) {
            System.out.println("descending");
        } else {
            System.out.println("mixed");
        }
    }


}
