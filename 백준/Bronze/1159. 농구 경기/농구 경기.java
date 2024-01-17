
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt( bufferedReader.readLine() );
        String[] arr = new String[N];

        for(int i = 0 ; i < N; i++) {
            arr[i] = bufferedReader.readLine();
        }

        Arrays.sort(arr);

        int left = 0;
        int right = 0;
        int cnt = 0;
        StringBuilder result = new StringBuilder();
        while(left < N){
            while(right < N && (arr[left].charAt(0) == arr[right].charAt(0)) && cnt < 5){
                right++;
                cnt++;
            }
            if(cnt == 5){
                result.append(arr[left].charAt(0));
            }
            cnt = 0;
            while(right < N && arr[left].charAt(0) == arr[right].charAt(0)){
                right++;
            }
            left = right;

        }

        if("".contentEquals(result)){
            System.out.println("PREDAJA");
        } else {
            System.out.println(result);
        }
    }


}

