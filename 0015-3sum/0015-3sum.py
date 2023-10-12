class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer = set()
        length = len(nums)
        nums.sort()
        
        for i in range(length-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            j = i+1
            k = length-1
            
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                    
                if three_sum > 0:
                    k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    answer.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    
                    
                    
        return answer
                
                