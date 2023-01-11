data = list(input())
target = list(input())

i = 0
cnt = 0
while i < len(data):

    if data[i] == target[0]:
        if ''.join(data[i:i+len(target)]) == ''.join(target):
            cnt += 1
            i += len(target)
        else:
            i+=1
    else:
        i+=1

print(cnt)
