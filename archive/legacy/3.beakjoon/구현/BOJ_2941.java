import java.util.*;
import java.io.*;

public class BOJ_2941 {
    public static void main(String[] args) throws Exception {
      String[] alpha = {"c=", "c-", "dz=","d-","lj","nj","s=","z="};

      BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
      String in = reader.readLine();

      for ( String a : alpha ) {
        String newIn = in.replace(a, "*");
        in = newIn;
      }
      System.out.println(in.length());
    }
}
