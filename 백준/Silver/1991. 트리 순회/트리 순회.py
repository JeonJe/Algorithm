class Node:
    def __init__(self, item,left,right):
        self.val = item
        self.left = left
        self.right = right

def pre_order(node):
    print(node.val, end='')
    if node.left != '.': pre_order(tree[node.left])
    if node.right != '.': pre_order(tree[node.right])

def in_order(node):
    if node.left != '.': in_order(tree[node.left])
    print(node.val, end='')
    if node.right != '.': in_order(tree[node.right])
    
def post_order(node):
    if node.left != '.': post_order(tree[node.left])
    if node.right != '.': post_order(tree[node.right])
    print(node.val, end='')


n = int(input())
tree = {}
for _ in range(n):
    val, left, right = input().split()
    tree[val] = Node(val,left,right)
    
pre_order(tree["A"])
print()
in_order(tree["A"])
print()
post_order(tree["A"])
print()