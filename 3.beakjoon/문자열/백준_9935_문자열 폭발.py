
string_stack=[]
bomb_stack = []

target_str = list(input())
bomb_str = list(input())

size_target_str = len(target_str)
size_bomb_str = len(bomb_str)

stack = []

for char in target_str:
    stack.append(char)
    if char == bomb_str[-1] and "".join(stack[-size_bomb_str:]) == "".join(bomb_str):
        del stack[-size_bomb_str:]


if len(stack) > 0:
    print("".join(stack))
else:
    print("FRULA")


