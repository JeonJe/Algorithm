import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());


        // n = 15라면 한 자리(최대 값 9)로는 안되고 최소 2자리부터 시작
        int k = (int) Math.ceil((double) n / 9);

 
            if (k % 2 == 0 && n % 2 != 0) {
                k++;
            } 
                System.out.println(k);
            

        br.close();
    }
}