import sys
# sys.stdin = open("input.txt",'rt') 

Max = -1

def DFS(Depth,sum,tsum):
    global Max
    #tsum 은 아직 확인하지 않은 부분집합 원소들의 합
    if sum+(total-tsum)  < Max :
        #지금까지 확인한 원소들의 합 + 
        # +전체 원소들의 합 
        # - 지금까지 확인한 원소들을 제외한 합이 이전에 구한 Max값보다
        #작으면 확인 필요 없음
     return 

    if sum > C:
        return 
    if Depth == N:
        if sum > Max:
            Max = sum
    else:
        DFS(Depth+1,sum+arr[Depth],tsum+arr[Depth])
        DFS(Depth+1,sum,tsum+arr[Depth])


if __name__ == "__main__":
    C,N = map(int,input().split())
    arr = [int(input()) for i in range(N)]
    total = sum(arr)
    DFS(0,0,0)
    print(Max)
