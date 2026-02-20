
n=int(input())

arr = [ int(input())for _ in range(n)]

arr.sort(reverse=True)

sum=[]
for i in range(n):
    sum.append(arr[i]*(i+1))
    # print(arr[i],i+1,arr[i]*(i+1))


res = max(sum)
print(res)
