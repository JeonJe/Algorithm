# dict = {0:"zero",1:"one", 2:"two", 3:"three",4:"four", 5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
# alphadict = {"zero":'0',"one":'1', "two":'2', "three":'3',"four":'4', "five":'5',"six":'6',"seven":'7',"eight":'8',"nine":'9'}

# res = []
# N,M = map(int,input().split())

# for i in range(N, M+1):
#     num = i
#     num_to_alpha = []
#     while num > 0:
#         digit = num % 10
#         num = num // 10
#         num_to_alpha.append(dict[digit])
#     num_to_alpha = num_to_alpha[::-1]
#     res.append(num_to_alpha)

# res.sort()

# i = 0
# for r in res:
#     temp = ''
#     for n in r:
#         temp+= alphadict[n]
#     print(int(temp),end=' ')
#     i+=1
#     if i == 10:
#         print()
#         i = 0

m, n = map(int, input().split())
change_dict = {'0': 'zero','1': 'one','2': 'two','3': 'three',
    '4': 'four','5': 'five','6': 'six','7': 'seven','8': 'eight',
    '9': 'nine'}

strs = [[] for i in range(n+1)]

num_dict = {}
for i in range(m, n+1):
    for j in str(i):
        strs[i].append(change_dict[j])

    strs[i] = ' '.join(strs[i])
    num_dict[strs[i]] = i
    

result = sorted(num_dict.items())

for j in range(len(result)):
    if (j+1) % 10 == 0:
        print(result[j][1])
    else:
        print(result[j][1], end = ' ')