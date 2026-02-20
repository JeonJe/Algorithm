import sys
# sys.stdin=open("input.txt", "r")

def DFS(level,start,s):
    global cnt
    if level == K:
       if s%M==0:
           cnt+=1
    else:
        for i in range(start,N):
            temp[level] = i
            DFS(level+1,i+1,s+arr[i])

if __name__ == "__main__":
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    M = int(input())
    cnt = 0
    temp = [0]*(N+1)

    DFS(0,0,0)
    print(cnt)


# n, k=map(int, input().split())
# a=list(map(int, input().split()))
# m=int(input())
# cnt=0
# for x in it.combinations(a, k):
#     if sum(x)%m==0:
#         cnt+=1
# print(cnt)
