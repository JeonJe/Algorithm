from tkinter import E


A, B, V = map(int, input().split())

#첫쩃날에 올라갈 수 있는지

 # 전체거리에서 첫쩃날 or 마지막 날 떨어지지 않는 거리  // 하루동안 오를 수 있는 거리 
day = (V-B)// (A-B)

#만약에 올라갈 수 있는 거리보다 더 많이 남았으면 하루 더 추가 
if (V-B) % (A-B) != 0:
    day+=1

print(day)


#몇일이 더 걸리는지?
