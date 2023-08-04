t = int(input())

for i in range(t):
    n = int(input())
    A = input()
    B = input()

    cnt_w, cnt_b = 0, 0
    for j in range(n):
        if A[j] == B[j]:
            continue
        elif A[j]  == "W":
            cnt_w += 1
        else:
            cnt_b += 1
    #b와 w를 교환
    min_b_w = min(cnt_w, cnt_b)
    cnt_w -= min_b_w 
    cnt_b -= min_b_w 

    answer = min_b_w + cnt_w + cnt_b
    print(answer)
            