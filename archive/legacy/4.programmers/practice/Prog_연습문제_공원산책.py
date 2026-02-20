def solution(park, routes):
    answer = []
    x,y = 0,0
    width = len(park[0])
    height = len(park)
    
    for i in range(height):
        for j in range(width):
            if park[i][j] == "S":
                x = i 
                y = j
    
    for route in routes:
        col_list  = []
        direct, distance = route.split()
        distance = int(distance)
        
        if direct == "E" and y + distance < width:
            if "X" not in list(park[x][y : y+distance+1]):
                y = y + distance
        elif direct == "W" and y - distance >= 0:
            if "X" not in list(park[x][y : y-distance-1]):
                y = y - distance
        elif direct == "S" and x + distance < height:
            for i in range(x,x+distance+1):
                col_list.append(park[i][y])
            if "X" not in col_list:
                x = x + distance
        elif direct == "N" and x - distance >= 0:
            for i in range(x,x-distance-1,-1):
                col_list.append(park[i][y])
            if "X" not in col_list:
                x= x - distance

    return [x,y]

park = ["OSO", "OOO", "OXO", "OOO"]
route =  ["E 2", "S 3", "W 1"]
print(solution(park,route))