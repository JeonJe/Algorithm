import java.util.*; 

class Solution {
    
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        
        // 다리 만들기
        Queue<Integer> bridge = new LinkedList<Integer>();
        for(int i = 0; i < bridge_length; i++) {
            bridge.add(0);
        }
        
        int time = 0;
        int currentWeight = 0;
        // 현재까지 몇 개의 트럭이 지나갔는지 표시 
        int idx = 0;
        
        // 지나갈 트럭이 있거나, 다리 위에 트럭이 있는 동안
        while(idx < truck_weights.length || currentWeight > 0) {
        // 시간이 지나고
            time++;
            
        // 다리 맨 끝 확인 
            int out = bridge.poll();
            currentWeight -= out;
            
        //다리 첫 번째 확인 
            if(idx < truck_weights.length) {
                // 새로운 트럭이 다리위에 올라감
                if(currentWeight + truck_weights[idx] <= weight) {
                    currentWeight += truck_weights[idx];
                    bridge.add(truck_weights[idx]);
                    idx++;
                } else {
                    bridge.add(0);
                }
            }
        }
        
    
    	return time;
	}	
}