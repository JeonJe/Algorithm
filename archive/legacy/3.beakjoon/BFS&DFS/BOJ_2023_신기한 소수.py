
def is_prime(candidate):
    for i in range(2, int(candidate**(1/2))+1):
        if candidate % i == 0:
            return False
    return True
            
def dfs(depth,path):
    if depth >= n:
        print( "".join(map(str,path)))
        return

    for i in [1,3,7,9]:
        path.append(i)
        target_num  = int("".join(map(str,path)))

        if is_prime(target_num):
            dfs(depth+1, path)

        path.pop()

n = int(input())

for i in [2,3,5,7]:
    dfs(1,[i])