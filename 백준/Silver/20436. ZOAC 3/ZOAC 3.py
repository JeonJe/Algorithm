

keyboard = [ 'qwertyuiop','asdfghjkl','zxcvbnm' ]

init_left, init_right = input().split()


def find_position(char):
    for idx, key in enumerate(keyboard):
      if char in key:
         return idx, key.index(char)
      
lx,ly = find_position(init_left)
rx,ry = find_position(init_right)

target = input()
right_hand = 'yuiophjklbnm'

answer = 0
for i in target:
  tx, ty = find_position(i)
  if i in right_hand:
     answer += abs(tx-rx) + abs(ty-ry)
     rx, ry = tx,ty
  else:
     answer += abs(tx-lx) + abs(ty-ly)
     lx, ly = tx,ty
  answer+=1

print(answer)

