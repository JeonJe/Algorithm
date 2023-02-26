import sys
input = sys.stdin.readline

first_string = list(input())
second_string = list(input())

lcs = [ [0]*(len(first_string)+1) for _ in range(len(second_string)+1) ]

for i in range(1,len(second_string)):
    for j in range(1,len(first_string)):
        if second_string[i-1] == first_string[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
                                                                                                                                                                                                                                                                                      

print(lcs[len(second_string)-1][len(first_string)-1])
