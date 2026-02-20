
try:
    while True:
    
        sub, standard = input().split()
        idx_sub, idx_standard = 0, 0
        
        while idx_sub < len(sub) and idx_standard < len(standard):
            if sub[idx_sub] == standard[idx_standard]:
                idx_sub += 1
                idx_standard += 1
            else:
                idx_standard += 1

        if idx_sub == len(sub) : 
            print("Yes")    
        else:
            print("No")
        
except:
    pass