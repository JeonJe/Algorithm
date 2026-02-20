from collections import defaultdict
import datetime 

def solution(today, terms, privacies):
    answer = []
    
    term = defaultdict(int)
    today_year, today_month, today_day = map(int,today.split("."))
    today_date = datetime.date(today_year, today_month, today_day)

    for t in terms:
        category, valid_month = t.split()
        term[category] = int(valid_month)
        
    i = 1
    for p in privacies:
        privacies_date, category = p.split()
        year, month, day = map(int, privacies_date.split("."))

        sum_year, sum_month = 0, 0
        #유효기간이 12개월 이상이면? year도 같이 올려야 함
        if term[category] >= 12:
            sum_year = term[category] // 12
            sum_month = term[category] % 12
        else:
            sum_month = term[category] 

        year += sum_year
        month += sum_month
        day -= 1
        #day가 0일 때 예외처리
        if day == 0:
            day = 28
            month -= 1
            
        #month을 올렸을 때 연도가 추가적으로 바뀌는지 확인
        if month > 12:
            month = month % 12
            if month == 0:
                month = 12
            year += 1
                
        expire_date = datetime.date(year,month,day)

        if expire_date < today_date:
            answer.append(i)
        i += 1

    #현재 시간과 비교해서 더 작은 날짜 수를 리턴 
    return answer



today = "2022.05.19"
terms =   ["A 6", "B 12", "C 3"]
privacies =  ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today,terms,privacies))