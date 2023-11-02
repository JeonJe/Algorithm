
#종말의 수 666, 1666, 2666 의 N번째 

n = int(input())

target = 666

while n:
    if '666' in str(target):
      n -= 1
    target += 1

print(target-1)