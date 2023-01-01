N,M,X,Y,K = map(int,input().split())

graph = [ list(map(int,input().split())) for _ in range(N)]

commands = list(map(int,input().split()))

global top,back,right,left,front,bottom
top, back, right, left, front, bottom = 0,0,0,0,0,0
def move_dice(direction):
    global top,back,right,left,front,bottom
    if direction == 1:
        top,left,bottom,right = right,top,left,bottom
    elif direction == 2:
        top,left,bottom,right = left,bottom,right,top
    elif direction == 3:
        top,front,bottom,back = front,bottom,back,top
    elif direction == 4:
        top,front,bottom,back = back,top,front,bottom

def diff(x,y):
    global bottom,top 

    if graph[x][y] == 0:
        graph[x][y] = bottom
    else:
        bottom = graph[x][y] 
        graph[x][y] = 0

#동 서 북 남
dx = [0,0,-1,1]
dy = [1,-1,0,0]


for direction in commands:
    point_x, point_y = X+dx[direction-1],Y+dy[direction-1]

    if point_x < 0 or point_y < 0 or point_x>= N or point_y>=M:
        continue
    move_dice(direction)
    diff(point_x, point_y)
    
    print(top)
    X = point_x
    Y = point_y





