from functools import cmp_to_key

n = int(input())

data = [ input() for _ in range(n) ]

def mysort(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    else:
        sum_a, sum_b = 0, 0

        for i in range(len(a)):
            if a[i].isdigit():
                sum_a += int(a[i])
        
        for j in range(len(b)):
            if b[j].isdigit():
                sum_b += int(b[j])
        
        if sum_a < sum_b:
            return -1
        elif sum_a > sum_b:
            return 1
        else:
            if (a > b):
                return 1
            elif (a < b):
                return -1
            else:
                return 0

        
        

data = sorted(data,key=cmp_to_key(mysort))

for i in data:
    print(i)