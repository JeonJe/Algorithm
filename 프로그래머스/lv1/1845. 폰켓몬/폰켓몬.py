from collections import defaultdict 

dict = defaultdict(int)
catch = defaultdict(int)

def solution(nums):
    answer = 0
    
    max_num = len(nums)//2 
    
    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = 1
        else:
            dict[nums[i]] += 1
    
    for n in dict:
        
        if n not in catch:
            # dict[n] -= 1
            catch[n] += 1
            answer+=1
        if answer >= max_num:
            return max_num
    return answer


