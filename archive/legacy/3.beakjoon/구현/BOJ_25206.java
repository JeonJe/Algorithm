import java.util.*;
import java.io.*;

public class BOJ_25206 {
  static HashMap<String, Double> map = new HashMap<String, Double>() {{
    put("A+", 4.5);
    put("A0", 4.0);
    put("B+", 3.5);
    put("B0", 3.0);
    put("C+", 2.5);
    put("C0", 2.0);
    put("D+", 1.5);
    put("D0", 1.0);
    put("F", 0.0);
  }};
  

  public static void main(String[] args) throws Exception {
    int length = 20;
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st; 
    double total = 0;
    double point_total = 0;
    for (int i = 0; i < length; i++) {
      st = new StringTokenizer(reader.readLine());
      String name = st.nextToken();
      double point = Double.parseDouble(st.nextToken());
      String Grade = st.nextToken();

      if (Grade.equals("P")) {
        continue;
      }
      double calculated = 0;
      for (Map.Entry<String, Double> entry : map.entrySet()) {
        
        if (Grade.equals(entry.getKey()))  {
          calculated = point * entry.getValue();
          break;
        }
      }
      total += calculated; 
      point_total += point;
    }
    double avg = total / point_total;
    System.out.printf("%.6f", avg);

  }
  
}
