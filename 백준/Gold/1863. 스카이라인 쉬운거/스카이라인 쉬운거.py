
n = int(input())

seq = [list(map(int,input().split())) for _ in range(n)]
stack = [0]

building_cnt = 0
for _, height in seq:
    if not stack:
        stack.append(height)
        building_cnt += 1
    else:
        if stack[-1] == height:
            continue
        elif stack[-1] < height:
            stack.append(height)
            building_cnt += 1
        else:
            while stack and stack[-1] > height:
              stack.pop()

            if stack and stack[-1] < height:
              stack.append(height)
              building_cnt += 1
print(building_cnt)