class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        for s in stones:
            if s not in freqs:
                freqs[s] = 1
            else:
                freqs[s] += 1

        cnt = 0

        for j in jewels:
            if j in freqs:
                cnt += freqs[j]
        return cnt

print(Solution().numJewelsInStones("aA","aAAbbbb"))