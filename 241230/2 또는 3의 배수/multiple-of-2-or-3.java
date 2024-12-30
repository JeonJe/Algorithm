import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        String result = "";
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int s = Integer.parseInt(br.readLine()); 
        
        for(int i = 1; i < s+1; i++) {
            if(i % 2 == 0 || i % 3 == 0) {
                result += "1 " ;
            } else {
                result += "0 ";
            }
        }
        System.out.print(result);
    
    }
}