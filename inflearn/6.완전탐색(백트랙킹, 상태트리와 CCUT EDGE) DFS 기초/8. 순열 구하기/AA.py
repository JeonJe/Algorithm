import sys
# sys.stdin = open("input.txt",'r') 

def DFS(L):
    global cnt
    if L==M:
        if len(set(res))==M:
            for i in res:   
                print(i,end=' ')
            print()
            cnt+=1
        return
    else:
        for i in range(N):
            res[L] = i+1
            DFS(L+1)
            
if __name__ == "__main__":
  N,M = map(int,input().split())
  cnt = 0
  res = [0]*M
  DFS(0)
  print(cnt)
