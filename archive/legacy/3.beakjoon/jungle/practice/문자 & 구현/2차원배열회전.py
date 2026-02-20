arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
right_arr_rotation = [list(reversed(i)) for i in zip(*arr)]
print(right_arr_rotation)

left_arr_rotation = [ list(i) for i in reversed(list(zip(*arr))) ]
print(left_arr_rotation)
