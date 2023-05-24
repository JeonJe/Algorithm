N, M = map(int,input().split())
seq = [list(map(int,input().split())) for _ in range(M)]

q = N // 6
r = N % 6
answer = 0
sort_by_package_price = list(sorted(seq))
sort_by_unit_price = list(sorted(seq, key=lambda x : x[1]))

answer += min(sort_by_package_price[0][0], sort_by_unit_price[0][1] * 6) * q
answer +=  min(sort_by_package_price[0][0], sort_by_unit_price[0][1] * r)    

print(answer)
