n = int(input())

seq = [ int(input()) for _ in range(n) ]
seq.sort()

answer = 0
for i in range(len(seq)):
    expect_rank = seq[i]
    #불만도 = 예상등수 - 실제 등수 
    dissatisfied = abs(expect_rank-(i+1))
    answer += dissatisfied

print(answer)

