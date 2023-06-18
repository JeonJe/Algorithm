N, M = map(int,input().split())
seq = [list(map(int,input().split())) for _ in range(M)]

q = N // 6
r = N % 6
answer = 0
sort_by_package_price = list(sorted(seq))
sort_by_unit_price = list(sorted(seq, key=lambda x : x[1]))

answer += min(sort_by_package_price[0][0], sort_by_unit_price[0][1] * 6) * q
answer +=  min(sort_by_package_price[0][0], sort_by_unit_price[0][1] * r)    
# while N > 0:

#     #최저 패키지 가격과, 최저 낱개 M개 가격을 비교하여 더 낮은 가격 선택
#     if N < 6:
#         answer += min(sort_by_package_price[0][0], sort_by_unit_price[0][1] * N)    
#         N = 0
#     #최저 패키지 가격과, 최저 낱개 6개 가격을 비교하여 더 낮은 가격 선택
#     else:
#         answer += min(sort_by_package_price[0][0], sort_by_unit_price[0][1] * 6)
#         N -= 6

print(answer)
