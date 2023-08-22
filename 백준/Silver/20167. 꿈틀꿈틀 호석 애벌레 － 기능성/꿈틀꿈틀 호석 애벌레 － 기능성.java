import java.util.*;
import java.io.*;

public class Main {
  static int answer = 0;
  static int N,K = 0;
  static int[] seq;
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    K  = Integer.parseInt(st.nextToken());

    seq = new int[N];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++){
      seq[i] = Integer.parseInt(st.nextToken());
    }

    dfs(0,0,0);
    System.out.println(answer);
    
  }
  static void dfs(int idx, int satisfaction, int energy){
    if (idx == N) {
      answer = Math.max(answer, energy);
      return ;
    }

    // i번째 애벌레 선택하지 않고 다음으로 넘어감
    dfs(idx+1, satisfaction, energy);

    if(satisfaction + seq[idx] >= K) {
      int getEnergy = satisfaction + seq[idx] - K;
      dfs(idx+1, 0, energy + getEnergy);
    } else{
      dfs(idx+1, satisfaction + seq[idx], energy);
    }

  }
}
