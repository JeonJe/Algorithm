from collections import defaultdict

n = int(input())
tot = int(input())

arr = list(map(int,input().split()))
dict = defaultdict(list)

for i in range(tot):
    cur_candi = str(arr[i])

    if cur_candi in dict:
        dict[cur_candi][0] += 1
    else:
        if len(dict) == n :
            sorted_dict = sorted(dict.items(), key=lambda x : (x[1][0], x[1][1]))
            del dict[sorted_dict[0][0]]
        dict[cur_candi] = [1,i]
        
sorted_dict = sorted(dict.items(), key=lambda x : int(x[0]))

for k, v in sorted_dict:
        print(k, end=' ')





