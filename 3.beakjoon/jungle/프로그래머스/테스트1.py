def check_qr(img,x,y,width,col,row):
    #가로, 세로,
    for i in range(width):
        if x+i >= row or y+i >= col or x+width-1 >= row:
            return False 
        #오른쪽
        if img[x][y+i] != '#':
            return False
        #오른쪽
        if img[x+width-1][y+i] != '#':
            return False 
        #아래
        if img[x+i][y] != '#':
            return False
        #아래
        if img[x+i][y+width-1] != '#':
            return False
   
    return True 



def solution(low, high, img):
    answer = 0

    #1.정사각형 확인
    col = len(img[0])
    row = len(img)
    # print(col,row)
    for i in range(row):
        for j in range(col):
            #한변의 길이 확인
            if img[i][j] == '#':
                width = 0
                k = j
                while  k <= col-1 and img[i][k] == '#':
                    width+=1
                    k+=1
                if width < 3: continue
                if check_qr(img,i,j,width,col,row):
                    # print('i,j,width')
                    # print(i,j,width)
                    
                    white, black = 0,0
                    for a in range(width-2):
                        for b in range(width-2):    
                            # print(img[i+1+a][j+1+b],end=' ')
                            if img[i+1+a][j+1+b] == '.':
                                white +=1
                            else:
                                black +=1
                        # print()
                    # print('low,mid,high')
                    # print(low ,((black / ((width-2) **2)) * 100), high)
                    if low<= ((black / ((width-2) **2)) * 100) < high :
                        answer+=1

    return answer


low = 0
high = 30
img = ["#####","##..#","#####","#####","#####" ]
# img = ["#######....###..###.", "#.....#....#.#..#.#.", "#.....#....###..###.", "#.....#.............", "#..#########........", "#..#..#....#.....##.", "#######....#.....##.", "...#.......#........", "...#.......#........", "...#..##############", "...#..#....#.......#", "...#..#....#.......#", "...#########.......#", "......#............#", "......##############"]

print(solution(low,high,img))