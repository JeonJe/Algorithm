import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws Exception{
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(reader.readLine());

    int A = Integer.parseInt(st.nextToken());
    int B = Integer.parseInt(st.nextToken());
    int[] seqA = new int[A];
    int[] seqB = new int[B];

    st = new StringTokenizer(reader.readLine());
    for (int i = 0; i < A; i++) {
      seqA[i] = Integer.parseInt(st.nextToken());
    }
    st = new StringTokenizer(reader.readLine());
    for (int i = 0; i < B; i++) {
      seqB[i] = Integer.parseInt(st.nextToken());
    }
    Arrays.sort(seqA);
    Arrays.sort(seqB);
    StringBuilder answer = new StringBuilder();
    int answerCount = 0;
    for (int i = 0; i < seqA.length; i++) {
      if ( binarySearch(seqB, seqA[i]) == false) {
        answerCount++;
        answer.append(seqA[i] + " ");
      }
    }
    if(answerCount == 0) {
      System.out.println("0");
    } else{
      System.out.println(answerCount);
      System.out.println(answer.toString());
    }
    
  }
  

  static boolean binarySearch(int[] arr, int target) {
    int left = 0;
    int right = arr.length-1;

    while (left <= right) {
      int mid = left + (right - left) / 2;
      if (arr[mid] == target) {
        return true;
      }
      else if (arr[mid] < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return false;
  }

  
}