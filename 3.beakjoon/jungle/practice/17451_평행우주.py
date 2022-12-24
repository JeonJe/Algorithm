n = int(input())

arr = list(map(int,input().split()))

if len(arr) == 1:
    print(arr[0])
    exit()

v = arr[-1]

for i in range(len(arr)-1, -1, -1):

    #현재 행성의 속도가 다음 행성의 속도보다 크면 현재 속도를 줄여서 도착할 수 있기 때문에
    #v 는 유지한다.
    if arr[i] > v:
        v = arr[i]
    else:
    # 300 400 500 400 300 에서 400(arr[i]) 500(v) 의 비교상황
    # 400은 500보다 작고, 두 사이는 배수관계가 아니기 때문에 500보다 큰 400의 배수를 v에 대입한다.
    #여기서는 400*2인 800이 500보다 크므로 v는 800이 된다.
    #마찬가지로 300 800 을 비교했을 때 300을 800보다 큰 300의 배수인 900으로 만들어준다.
        if arr[i] < v and v % arr[i] != 0:
            v = ((v // arr[i]) + 1 ) * arr[i]
        
print(v)
