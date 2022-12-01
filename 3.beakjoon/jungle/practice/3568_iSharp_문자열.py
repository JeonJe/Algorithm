import sys 

sys.stdin.readline

isharp = input().rstrip()

split = isharp.split(' ')
split_len = len(split)
b_type = split[0]

type = [[] for _ in range(split_len)]
value = [[]for _ in range(split_len)]

for i in range(1,len(split)):
    c = split[i]
    c = list(c.replace(',','').replace(';',''))
    temp_type = ""
    temp_value = ""
    first = c[-1]

    for j in range(len(c)-1, -1, -1):
        if not first.isalpha():
            if c[j].isalpha():
                temp_value+=c[j]
            else:
                if c[j] == "]":
                    c[j] = "["
                elif c[j] == "[":
                    c[j] = "]"
                temp_type+=c[j]
        else:
            if c[j].isalpha():
                temp_value+=c[j]
            else:
                temp_type+=c[j]

    temp_value = ''.join(list(reversed(temp_value)))
    
    type[i] = temp_type
    value[i] = temp_value

for i in range(1,split_len):
    print(f'{b_type}{type[i]} {value[i]};')