import sys 

class Queue:
    def __init__(self,X):
        self.first = 0
        self.rear = 0
        self.no = 0
        self.capacity = X
        self.que = [None] * X 

    def push(self,X):
        self.que[self.rear] = X
        self.rear += 1
        self.no += 1
        
         
    def pop(self):
        if self.no <= 0:
            return -1
        x = self.que[self.first]
        self.first += 1
        self.no -= 1
        return x 
    
    def empty(self):
        if self.no <= 0:
            return 1
        return 0

    def size(self):
        return self.no

    def front(self):
        if self.empty():
            return -1
        return self.que[self.first]

    def back(self):
        if self.empty():
            return -1
        return self.que[self.rear-1]

N = int(input())
que = Queue(N)

for _ in range(N):
    line = sys.stdin.readline().split()
    
    #push
    if len(line) > 1:
        ins, num = line[0], int(line[1])
        que.push(num)
    else:
        ins = line[0]
        if ins  == "front":
            print(que.front())
        if ins  == "back":
            print(que.back())
        elif ins == "size":
            print(que.size())
        elif ins == "empty":
            print(que.empty())
        elif ins == "pop":
            print(que.pop())
    