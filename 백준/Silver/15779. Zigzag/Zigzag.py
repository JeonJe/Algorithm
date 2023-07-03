n = int(input())
seq = list(map(int,input().split()))

max_length, current_length = 2, 2 

for i in range(len(seq)-2):
    if seq[i] <= seq[i+1] <= seq[i+2] or  seq[i] >= seq[i+1] >= seq[i+2]:
        current_length = 2
    else:
        current_length += 1
    
    max_length = max(max_length, current_length)

print(max_length)

        