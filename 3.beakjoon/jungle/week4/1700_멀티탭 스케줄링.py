
n, k = map(int,input().split())

orders = list(map(int,input().split()))
multab = []

cnt = 0 
for i in range(len(orders)):
    #지금 현재 확인하고 있는 전기용품이 멀티탭에 이미 꽂혀있으면 continue
    if orders[i] in multab:
        continue
    else:
        #현재 사용하려고 하는 전기 용품을 멀티탭에 꽂아야 할 때

        #멀티탭이 꽉차있는 경우 
        if len(multab) == n:
            #현재 확인중인 전기 용품 뒤로 멀티탭에 꽂힌 전기 용품이 또 쓰이는 지 확인
            all_used = True
            for j in range(len(multab)):
                #뒤에도 현재 확인 중인 전기 용품이 쓰이면 pass
                if multab[j] in orders[i+1:]:
                    continue
                else:
                    all_used = False
                    multab[j] = orders[i]
                    cnt+=1
                    break
            
            #만약 멀티탭에 쓰인 애들이 모두 뒤쪽에서 사용하고 있으면
            #가장 늦게 사용되는 걸 뺴자 
            if all_used:
                latest_index  = -1 
                for k in range(len(multab)):
                    latest_index = max(latest_index, orders[i+1:].index(multab[k]))    
                latest_value = orders[i+1:][latest_index]
                update_index = multab.index(latest_value)
                multab[update_index] = orders[i]
                cnt+=1
        
        #멀티탭이 꽉차있지 않는 경우 
        else:
            multab.append(orders[i])

print(cnt)


