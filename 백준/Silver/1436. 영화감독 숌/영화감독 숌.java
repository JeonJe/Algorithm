import java.io.*;

public class Main {
  public static void main(String[] args) throws Exception{
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(reader.readLine());

    int target = 666;
    while (N > 0){
      String temp = Integer.toString(target);
      if (temp.contains("666")){
        N -= 1;
      }
      target += 1;
    }
    target -= 1;
    System.out.println(target);
  }
}
