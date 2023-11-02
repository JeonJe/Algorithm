class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            v = temperatures[i]
            
            #현재 확인 중인 값이 이전 스택에 쌓인 값보다 
            #현재 위치와 이전 스택이 가리키는 거리를 계산하여 저장
            #스택을 pop하고도 스택에 남아있는 값이 현재 더 낮다면 계속 갱신 
            while stack and v > stack[-1][0]:
                prev_v, prev_index = stack.pop()
                answer[prev_index] = i - prev_index
                
            stack.append((v, i))
        return answer 
    
                
            
            
                            

