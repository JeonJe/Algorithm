n = int(input())

box_list = list(map(int,input().split()))
dp=[1]*(n+1)

max_num = -1
for i in range(n):
    for j in range(i):
        if box_list[j] < box_list[i] and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1
        max_num = max(max_num,dp[i])
        # print('i : ', i, ' j = ', j, ' dp :', dp, box_list)

print(max_num)
