scores = {
    'A+': 4.3,
    'A0': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B0': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C0': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D0': 1.0,
    'D-': 0.7,
    'F': 0.0
}

def custom_round(avg, digits):
    return round(avg + 10**(-len(str(avg))-1), digits)
n = int(input())
seq = [list(input().split()) for _ in range(n)]

total = 0
temp = 0
for i in range(n):
    total += int(seq[i][1]) * scores[seq[i][2]]
    temp += int(seq[i][1])

print(f'{custom_round(total / temp , 2):.2f}')