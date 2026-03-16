import java.io.BufferedReader;
  import java.io.InputStreamReader;
  import java.util.Arrays;

  public class Main {

      static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      static boolean[] visited = new boolean[10];
      static long[] list = new long[8_877_700];
      static int listIdx = 0;

      public static void main(String[] args) throws Exception {
          for (int i = 1; i <= 9; i++) {
              visited[i] = true;
              dfs(i);
              visited[i] = false;
          }

          Arrays.sort(list, 0, listIdx);

          StringBuilder sb = new StringBuilder();
          String input;
          while (!(input = br.readLine()).equals("0")) {
              int idx = Integer.parseInt(input);
              sb.append(list[idx - 1]).append('\n');
          }
          System.out.print(sb);
      }

      private static void dfs(long num) {
          list[listIdx++] = num;
          if (num > 9_876_543_210L) return;
          for (int i = 0; i <= 9; i++) {
              if (!visited[i]) {
                  visited[i] = true;
                  dfs(num * 10 + i);
                  visited[i] = false;
              }
          }
      }
  }
