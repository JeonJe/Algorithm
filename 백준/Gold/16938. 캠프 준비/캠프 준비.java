import java.io.*;
import java.util.*;

class Main {
  static int N,L,R,X;
  static int[] problems;
  static int answer; 

  public static void main(String args[]) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    L = Integer.parseInt(st.nextToken());
    R = Integer.parseInt(st.nextToken());
    X = Integer.parseInt(st.nextToken());

    problems = new int[N];
    
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++){
      problems[i] = Integer.parseInt(st.nextToken());
    }

    Arrays.sort(problems);

    dfs(0,-1,-1,-1,0);
    System.out.println(answer);
  }

  static void dfs(int depth, int idx, int minDifficult, int maxDifficult, int difficultSum) {
    if (difficultSum > R) {
      return ;
    }
    if ( L <= difficultSum && R >= difficultSum && depth >= 2 && maxDifficult - minDifficult >= X){
      answer++;
    }

    for (int i = idx+1; i < N; i++) {
        if (minDifficult == -1){
          dfs(depth+1, i, problems[i], maxDifficult, difficultSum + problems[i]);
        } else {
          dfs(depth+1, i, minDifficult, problems[i], difficultSum + problems[i]);
        }
    }
  }

}