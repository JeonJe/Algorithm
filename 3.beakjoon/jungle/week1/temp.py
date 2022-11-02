def Qsort(lt, rt):
        if lt < rt:
            pos = lt
            pivot =  arr[rt]
            for i in range(lt,rt):
                if arr[i] <= pivot:
                    arr[i], arr[pos] = arr[pos], arr[i]
                    pos += 1
            arr[rt], arr[pos] = arr[pos] , arr[rt]
        return 