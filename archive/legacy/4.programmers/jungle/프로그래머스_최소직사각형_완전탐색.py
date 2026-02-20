def solution(sizes):
    answer = 0
    width = []
    height = []
    for i in range(len(sizes)):
        sizes[i].sort(reverse=True)
        width.append(sizes[i][0])
        height.append(sizes[i][1])
        
    return max(width) * max(height)