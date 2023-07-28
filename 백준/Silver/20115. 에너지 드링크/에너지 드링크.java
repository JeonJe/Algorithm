import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));        
        
        int N = Integer.parseInt(br.readLine());
        int [] arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int maxValue = 0;
        for (int i = 0; i < N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
            if (arr[i] > maxValue) {
                maxValue = arr[i];
            }
        }
        
        double result = maxValue;
        for (int i = 0; i < N; i++){
            if (arr[i] != maxValue){
                result += arr[i] / 2.0;
            }
        }
        System.out.println(result);            
    }  
}
