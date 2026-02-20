import sys
sys.setrecursionlimit(100000)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST():
    def __init__(self, root):
        self.head = root

    def insert(self, Node):
        if self.head == None:
            self.head = Node
            return 
        else:
            self.insert_position = self.head

            #왼쪽으로 이동해야 한다면 
            while True:
                if Node.val < self.insert_position.val:
                    if self.insert_position.left != None:
                        self.insert_position = self.insert_position.left
                        continue
                    else:
                        self.insert_position.left = Node
                        break
                if Node.val > self.insert_position.val:
                    if self.insert_position.right != None:
                        self.insert_position = self.insert_position.right
                        continue
                    else:
                        self.insert_position.right = Node
                        break
            return self.head
                    
    def post_order(self, Node):
        
        if Node.left != None:
            self.post_order(Node.left)
        if Node.right != None:
            self.post_order(Node.right)
        print(Node.val)


arr = []

while True:
    try:
        n = int(input())
        arr.append(n)
    except:
        break

root = Node(arr[0])
bst = BST(root)

for i in range(1,len(arr)):
    cur = Node(arr[i])
    bst.insert(cur)

bst.post_order(root)