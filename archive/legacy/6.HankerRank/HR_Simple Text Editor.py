
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
history = []
st = ''
for _ in range(n):
    ops = input()
    if len(ops) > 1:
        ops, param = ops.split()
    
    #append w
    if ops == "1":
        st += param
        history.append([ops,param])
    #delete k
    elif ops == "2":
        history.append([ops,st[-int(param):]])
        st = st[:-int(param)]
    #print(k)
    elif ops == "3":
        if len(st) >= int(param)-1:
            print(st[int(param)-1])
    #undo 
    else:
        if history:
            command, p = history.pop()
            if command == "1":
                st = st[:-len(p)]
            else:
                st += p
    