import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Deque<int[]> queue = new ArrayDeque<>();
        for(int i = 0; i < priorities.length; i++) {
            queue.add(new int[]{i, priorities[i]});
        }
        
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            int curIdx = cur[0];
            int curPriority = cur[1];
            
            if(isGreater(curPriority, queue)) {
                queue.add(cur);
            } else {
                answer++;
                      
                if(curIdx == location) {
                    return answer;
                 } 
            }
      
        }
        return answer;
    }
    
    private boolean isGreater(int priority, Deque<int[]> queue) {
        for(int[] q : queue) {
            if(q[1] > priority) {
                return true; 
            }
        }
        return false;
    }
}