class Solution:
    def countAndSay(self, n: int) -> str:
        cnt = 1
        res = ""
        if n == 1:
            return "1"
        #문자열
        prev = self.countAndSay(n-1)
        for i in range(len(prev)):
            #마지막 문자 또는 다음 문자와 같지 않는 경우
            if i == len(prev) - 1 or prev[i] != prev[i+1]:
                # 카운팅한 갯수 + prev[i]
                res += str(cnt) + prev[i]
                cnt = 1
            else:
                cnt += 1
        return res