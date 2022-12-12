    if x >=y :
                yellow_x = x-2
                yellow_y = y-2
                yellow_total = yellow_x * yellow_y
                if brown == total_area - yellow_total:
                    print(x,y)
                    continue
