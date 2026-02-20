w, h = map(int,input().split())

T = int(input())
y_points = [0,h]
x_points = [0,w]

for i in range(T):
    select, point = map(int,  input().split())
    
    if select == 0:
        y_points.append(point)
    else:
        x_points.append(point)
x_points.sort(), y_points.sort()
# print(y_points, x_points)

diff = 0
diff2 = 0
for i in range(1,len(y_points)):
    diff = max(y_points[i] - y_points[i-1], diff)

for j in range(1,len(x_points)):
    diff2 = max(x_points[j] - x_points[j-1], diff2)


print(diff*diff2)

