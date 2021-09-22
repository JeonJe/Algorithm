import sys
# sys.stdin = open("input.txt",'r') 
input = sys.stdin.readline

def DFS(L):
    global cnt
 
    if L == M:
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
    res = [0]*M
    cnt = 0
    DFS(0)
    print(cnt)

