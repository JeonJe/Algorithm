import sys
# sys.stdin = open("input.txt",'r') 

def DFS(L):
    global cnt
    if L==M:
        for i in res:   
            print(i,end=' ')
        print()
        cnt+=1
        return 
           
    else:
        for i in range(1,N+1):
            if ch[i] == 0:
                ch[i] =1
                res[L] = i
                DFS(L+1)
                ch[i]=0
  
if __name__ == "__main__":
  N,M = map(int,input().split())
  cnt = 0
  res = [0]*M
  ch = [0]*(N+1)
  DFS(0)
  print(cnt)
