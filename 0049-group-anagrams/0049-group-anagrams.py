from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        anagrams = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            anagrams[sorted_s].append(s)
        
        sorted_by_length = list(sorted(anagrams.items(), key=lambda x : (len(x[1]))))
        for k ,v in sorted_by_length:
            sorted_v = list(sorted(v))
            answer.append(sorted_v)
        return answer

        



        