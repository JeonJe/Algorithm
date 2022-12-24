target = int(input())

m = int(input())

not_working = list(map(int,input().split()))
possible_channel = 1000000
# '+' 또는 '-'만 사용하여 가는 경우 
min_count = abs(target-100)

for channel in range(possible_channel):
  # 5457
  channel = str(channel)

    #채널의 모든 문자가 누를 수 있는 버튼이라면 타겟과 현재 누를 수 있는 채널의 차이 계산
  for c in range(len(channel)):
    if int(channel[c]) in not_working:
      break
    
    elif c == len(channel)-1:
        min_count = min(min_count, abs(int(channel)-target) + len(channel))

print(min_count)