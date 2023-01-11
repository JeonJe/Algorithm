A,B = map(int,input().split())

list_A = list(map(int,input().split()))
list_B = list(map(int,input().split()))

A_sub_B = set(list_A) - set(list_B)
B_sub_A = set(list_B) - set(list_A)
print(len(A_sub_B)+len(B_sub_A))