up, down, height = map(int,input().split())

cur = 0
day = 1
going = up - down 

#달팽이 day1 위치 
cur += up 
height = height - up

day += height // going 

#낮에 한번 더 올라가서 정상에 도달하는 경우 
if height % going != 0:
    day+=1

print(day)