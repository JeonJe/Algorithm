
before = input()

#c++ 형태면 1
#자바 형태면 2 
# 아무것도 아니라면 0
def check(before):
    temp = before
    # _를 포함하는 파이선 형태라면?
    if "_" in before:
        # _ 를 delimeter로 단어를 자름
        sp = list(temp.split('_'))
        for s in sp:
            #단어가 소문자 인지 확인
            if not s.islower():
                return 0
        return 1
    #자바 형태 
    else:
        if not temp[0].islower():
            return 0
        return 2
def translate(before, case):
    #c++ -> java
    temp = before
    ans = ""
    if case == 1:
        sp = list(temp.split('_'))
        ans += sp[0]
        for i in range(1,len(sp)):
            s = list(sp[i])
            s[0] = s[0].upper()
            ss = ''.join(s)
            ans += ss
        return ans
    #java -> c++
    else:
        temp_list = list(temp)
        for i in range(len(temp_list)):
            if temp_list[i].isupper():
                temp_list[i] = '_' + temp_list[i].lower()
        return ''.join(temp_list)



if check(before) == 1:
    print(translate(before, 1))
elif check(before) == 2:
    print(translate(before, 2))
else:
    print("Error!")