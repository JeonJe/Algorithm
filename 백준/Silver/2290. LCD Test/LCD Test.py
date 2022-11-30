import sys 
input = sys.stdin.readline

r = '-'
c = '|'

#ok
def top(digital_num):
    for i in range(1,s+1):
        digital_num[0][i] = r

#ok
def tr(digital_num):
    for i in range(1,s+1):
        digital_num[i][-1] = c
#ok
def tl(digital_num):
    for i in range(1,s+1):
        digital_num[i][0] = c
#ok
def md(digital_num):
    for i in range(1,s+1):
        digital_num[s+1][i] = r

def bottom(digital_num):
    for i in range(1,s+1):
        digital_num[2*s+2][i] = r

def br(digital_num):
    for i in range(s+2,2*s+2):
        digital_num[i][-1] = c

def bl(digital_num):
    for i in range(s+2, 2*s+2):
        digital_num[i][0] = c

def draw(c, digital_num):
    if c in [0, 2, 3, 5, 6, 7, 8, 9]:
        top(digital_num)
    if c in [0,4, 5, 6, 8, 9]:
        tl(digital_num)
    if c in [0,1,2,3,4,7,8,9]:
        tr(digital_num)
    if c in [2,3,4,5,6,8,9]:
        md(digital_num)
    if c in [0,2,6,8]:
        bl(digital_num)
    if c in [0,1, 3,4,5,6,7,8,9]:
        br(digital_num)
    if c in [0,2,3,5,6,8,9]:
        bottom(digital_num)

s,n = input().split()
s = int(s)
n = n.rstrip()

arr = []

for z in n:
    digital_num = [[' '] * (s+2) for _ in range(2*s+3)]
    draw(int(z), digital_num)
    arr.append(digital_num)

ans = [[] for _ in range(2*s + 3)]

for i in range(0, 2*s + 3):
    for idx in range(len(arr)):
        ans[i] += arr[idx][i]
        ans[i].append(' ')


for c_arr in ans:
    print(''.join(c_arr))