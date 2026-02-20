import sys
import itertools as it
# sys.stdin = open("input.txt",'r') 
  
def DFS(L,sum):
    if L==n and sum == f:
        for x in p:
            print(x, end=' ')
        print()
        sys.exit(0)
        #가장 처음에 나오는 순열이 제일 작음 
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1,sum+(p[L]*b[L]))
                #target값을 구하기 위해 각 이항계수와 순열 값을 곱해서 sum에 더함 
                ch[i]=0

if __name__ == "__main__":
    n,f = map(int,input().split())
    p=[0]*n #순열만들기
    b=[1]*n #이항계수
    ch=[0]*(n+1) #순열을 만들기 위한 배열, 중복 체크
    
    for i in range(1,n):
        b[i] = b[i-1]*(n-i) // i
        #각 이항계수, 분모는 앞의 수에 n-i를 곱하고 분자에는 i 나누기 

    a = list(range(1,n+1))
    # DFS(0,0)

    for tmp in it.permutations(a):
        sum=0
        for L,x in enumerate(tmp):
            sum += (x*b[L])
        if sum == f:
            for x in tmp:
                print(x,end=' ')
            break
                   ㅌ