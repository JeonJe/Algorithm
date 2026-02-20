class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left = 0
        right = len(height)-1
        
        while (left < right):
            current_height = 0
        
            if height[right] > height[left]:
                current_height = height[left]
            else:
                current_height = height[right]
            answer = max(answer, current_height * (right - left ))
            
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return answer 
            