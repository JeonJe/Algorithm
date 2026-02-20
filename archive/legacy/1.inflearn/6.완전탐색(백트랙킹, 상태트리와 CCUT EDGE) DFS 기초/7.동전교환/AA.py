import sys
# sys.stdin = open("input.txt",'r') 


def DFS(L,sum):
    global MIN  
    if L > MIN:
        return 

    if sum > target:
        return 

    if sum == target:
        if MIN > L:
            MIN = L
        
    else:
        for i in res:
            DFS(L+1,sum+i)

 
        


if __name__ == "__main__":
    MIN = 99999999
    N = int(input()) # 동전 종류의 개수 
    res = list(map(int,input().split())) #동전 리스트 
    res.sort(reverse=True)
    target = int(input()) #거스름돈
    
    DFS(0,0)
    print(MIN)

    
