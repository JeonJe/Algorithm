import java.util.Arrays;

class Solution {
    
    public boolean check(int[] enemy, int n, int k){
        if ( k >= enemy.length ){
            return true;
        }
        for(int i = 0; i < k; i++){
            enemy[i] = 0;
        }
        int sum = 0;
        for (int e : enemy){
            sum += e;
        }
        return sum <= n;
    }
    
    public int solution(int n, int k, int[] enemy) {
        int left = 0;
        int right = enemy.length+1;

        while( left + 1 < right){
            int mid = (left + right) / 2;
            int[] current_rocks = Arrays.copyOfRange(enemy, 0, mid);
            if (check(current_rocks, n, k)) {
                left = mid;
            }else{
                right = mid;
            }
        }
    }
    
    
}