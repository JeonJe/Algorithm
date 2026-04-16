 import java.io.BufferedReader;                                                          
  import java.io.InputStreamReader;                    
  import java.util.StringTokenizer;                                                       
                                                                                          
  public class Main {                               
      public static void main(String[] args) throws Exception {                           
          BufferedReader br = new BufferedReader(new InputStreamReader(System.in));     
          int t = Integer.parseInt(br.readLine().trim());                                 
          StringBuilder sb = new StringBuilder();                                         
                                                                                          
          for (int i = 0; i < t; i++) {                                                   
              StringTokenizer st = new StringTokenizer(br.readLine());
              int pos = Integer.parseInt(st.nextToken());                                 
              String s = st.nextToken();                       
              sb.append(s, 0, pos - 1).append(s.substring(pos)).append('\n');             
          }                                                                               
                                                                                          
          System.out.print(sb);                                                           
      }                                                        
  }       