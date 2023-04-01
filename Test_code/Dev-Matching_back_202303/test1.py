from collections import defaultdict 

def solution(wall):

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
     
    answer = []
    dict = defaultdict(set)
    height = len(wall)
    width = sum(map(int,wall[0].split()))
    #2차원 배열 생성
    graph = [ [[-1,-1] for _ in range(width)] for _ in range(height)]
    
    for i in range(len(wall)):
        rows = list(map(int,wall[i].split()))
        cur_point = 0
        for j in range(len(rows)):
            for k in range(rows[j]):
                graph[i][cur_point+k][0] = i
                graph[i][cur_point+k][1] = j
            cur_point += rows[j]
    
    for i in range(height):
        for j in range(width):
            key = str(graph[i][j][0])+","+str(graph[i][j][1])
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < height and 0 <= ny < width and graph[nx][ny] != graph[i][j]:
                    dict[key].add((graph[nx][ny][0],graph[nx][ny][1]))
                
    #중요한블록이 무엇인지 판단
    sorted_dict = sorted(dict.items(), key=lambda x : len(x[1]), reverse=True)
    import_block_size = len(sorted_dict[0][1])
    for key, value in sorted_dict:
        if len(value) == import_block_size:
            x,y = map(int,key.split(","))
            answer.append([x,y])
            
    return answer