import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static List<Long> list = new ArrayList<>();

    public static void main(String[] args) throws Exception {

        int n = Integer.parseInt(br.readLine());
        String[] arr = new String[n];
        for(int i = 0; i < n; i++) {
            arr[i] = br.readLine();
        }

        Arrays.sort(arr, Comparator.comparingInt(String::length).thenComparing(String::compareTo));

        for (String s : arr) {
            if(s.length() >= 3) {
                System.out.println(s);
                return;
            }
        }

    }


}