
def fun(ins):
    upper = 0
    lower = 0
    num = 0
    space = 0

    for i in list(ins):
        if i.isdigit():
            num+=1
        elif i.islower():
            lower+=1
        elif i.isupper():
            upper+=1
        else:
            space+=1
    print(lower, upper, num, space)
while True:
    try:
        ins=input()
        ans = fun(ins)
 
    except EOFError:
        break