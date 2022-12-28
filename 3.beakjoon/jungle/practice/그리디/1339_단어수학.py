from collections import defaultdict

n = int(input())

infos = [ list(input()) for _ in range(n) ]
dict = defaultdict(int)
first_number = ""
second_number = ""

def find_number(infos):
    # 어느 알파벳이 가장 자릿수가 높은지 확인을 해야한다.

    for info in infos:
        len_info = len(info)
        # 알파벳의 자릿수로 가중치를 확인한다.
        for i in range(len_info):
            dict[info[i]] += 10 ** (len_info - 1 - i)
    # 가중치가 높은 알파벳부터 정렬
    sorted_dict = sorted(dict.items(), key= lambda x : -x[1])
    # 그리디 알고리즘으로 가중치가 높은 알파벳부터 높은 숫자 부여
    priority = 9 
    for key,value in sorted_dict:
        dict[key] = priority
        priority -= 1
        

find_number(infos)

sum = 0
for info in infos:
    s = ""
    for i in list(info):
       s += str(dict[i]) 
    sum += int(s)

print(sum)