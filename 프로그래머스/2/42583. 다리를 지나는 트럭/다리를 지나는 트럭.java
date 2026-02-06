import java.util.*; 

class Solution {
    
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        
   		Queue<Integer> bridges = new LinkedList<>(); 
        for(int i = 0; i < bridge_length; i++) {
            bridges.add(0);
        }
        
        int time = 0;
        int currentWeight = 0;
        //몇번째 트럭까지 보냈는지 
        int idx = 0;
        
        //보낼 트럭이 남아있거나, 아직 트럭이 다 내리지 못한 경우 
        while(idx < truck_weights.length || currentWeight > 0) {
            time++;
            
            // 트럭이 끝에 도달했으면 내림 -> 큐의 마지막을 그냥 꺼내버림 
            int out = bridges.poll();
            currentWeight -= out;
            
            // 다음트럭이 올라올 수 있는 지 확인 
        	if(idx < truck_weights.length) {
                if(currentWeight + truck_weights[idx] <= weight) {
                    bridges.add(truck_weights[idx]);
                    currentWeight += truck_weights[idx];
                    idx++;
                } else {
                    bridges.add(0);
                }
            }
        }
        
        return time;
    }
}