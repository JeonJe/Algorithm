from collections import defaultdict 

class Solution:
    
    
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        answer = []
        def dfs(candis):
            if candis['('] == candis[')'] == 0:
                answer.append("".join(stack))
                return
            
            if candis['('] > 0:
                stack.append('(')
                candis['('] -= 1
                dfs(candis)
                candis['('] += 1
                stack.pop()
            if candis['('] < candis[')']:
                stack.append(')')
                candis[')'] -= 1
                dfs(candis)
                stack.pop()
                candis[')'] += 1
                    
            
            
        candis = defaultdict(int)
        candis['('] = n
        candis[')'] = n
        dfs(candis)
        
        return answer