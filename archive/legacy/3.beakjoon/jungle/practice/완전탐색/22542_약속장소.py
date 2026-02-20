import sys
input = sys.stdin.readline 

n, l = map(int,input().split())
remember = list(input() for _ in range(n))

answer = []

#depth에 current라는 알파벳을 넣었을 때 이름 후보 조건을 만족하는지 
def check(depth, path):
    for i in range(n):
        diff = 0
        for j in range(depth+1):
            if remember[i][j] != path[j]:
                diff += 1
        if diff >= 2:
            return False
    return True
        
def dfs(depth, path):
    if depth >= l:
        answer.append("".join(path))
        return 

    for i in range(26):
        cur = chr(ord('A') + i)
                
        path.append(cur)
        if check(depth,path):
            dfs(depth+1, path)
        path.pop()

dfs(0,[])

print(answer[0] if len(answer) >= 1 else "CALL FRIEND")