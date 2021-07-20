import sys

# sys.stdin = open("input.txt",'rt')

#랜선의 총 길이 입력받음
def Count(length):
    cnt = 0 

    #랜선의 길이에서 랜선의 총길이로 나눈 몫을 넣는다.
    for i in arr:
        cnt+= (i//length)
    return cnt
#이미 가지고 있는 랜선의 개수 K 
#필요한 랜선의 개수 N

K,N = map(int,input().split())

arr = [int(input()) for _ in range(K)]

longest = max(arr)

res = 0
left = 1
right = longest

# 1부터 '가지고있는 랜선' 중 제일 긴 랜선 길이 사이에서 랜선의 최대 길이가 될 수 있는 길이를 찾아함
# 확인할 mid 숫자를 가지고 Count 함수에 넣어 조건 만족 여부 확인!

while left <= right:
    target = (left + right) // 2

    if Count(target) >= N:
        res = target
        #랜선의 총 길이를 키워도 됨
        left = target+1
    
    else:
        #랜선의 총 길이를 낮춰야 됨
        right = target -1

print(res)