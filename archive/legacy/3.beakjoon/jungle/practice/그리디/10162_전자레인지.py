
n = int(input())
T = [300,60,10]

used = False
buttons = [0,0,0]


for i in range(len(T)):
    if n - T[i] >= 0:
        buttons[i] += n // T[i] 
        n = n % T[i]

if sum(buttons) <= 0 or n > 0:
    print(-1)
else:
    print(*buttons)




