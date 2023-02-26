n = int(input())

nums = list(map(int, input().split()))
target = int(input())

nums.sort()  # 두 수 사이에 있는 n을 찾아야 하므로 정렬

if target in nums:
    print(0)
    
else:
    min = 0
    max = 0
    for num in nums:            # 배열중에서 n과 가장 근접한 두 수를 구한다.
        if num < target:     
            min = num
        elif num > target and max == 0:
            max = num
    max -= 1                    # 1과 7사이에 n이 2이면 1과 7은 제외
    min += 1
    print((target-min)*(max-target+1) + (max-target))
    # n보다 작은 수와 만족할 경우 + n보다 큰 수와 만족할 경우