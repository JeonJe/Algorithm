import sys

class Stack:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self, N):
        self.stk = [None] * N
        self.ptr = 0
        self.capacity = N
        
    def size(self):
        return self.ptr

    def empty(self):
        if self.ptr <= 0:
            return 1
        else:
            return 0

    def full(self):
        return self.ptr >= self.capacity 

    def push(self, X):
        if self.full():
            raise Stack.Full
        self.stk[self.ptr] = X 
        self.ptr+=1

    def pop(self):
        if self.empty():
            return -1
        self.ptr -= 1
        return self.stk[self.ptr]

    def top(self):
        if self.empty():
            return -1
        return self.stk[self.ptr-1]

N = int(input())
stk = Stack(N)

for _ in range(N):
    line = sys.stdin.readline().split()
    
    #push
    if len(line) > 1:
        ins, num = line[0], int(line[1])
        stk.push(num)
    #top,size,empty,pop
    else:
        ins = line[0]
        if ins  == "top":
            print(stk.top())
        elif ins == "size":
            print(stk.size())
        elif ins == "empty":
            print(stk.empty())
        elif ins == "pop":
            print(stk.pop())
    