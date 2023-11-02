from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        dict = defaultdict(int)
        for n in nums:
            dict[n] += 1
        
        sorted_dict = list(sorted(dict.items(), key=lambda x : -x[1]))
        cnt = 1
        for key, v in sorted_dict:
            answer.append(key)
            if cnt == k :
                 break
            cnt+=1
        return answer

        