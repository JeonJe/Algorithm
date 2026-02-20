from collections import defaultdict 
import math 

def solution(fees, records):
    answer=[]
    in_time = defaultdict(int)
    prices = defaultdict(int)
    
    for i in range(len(records)):
        hm, car_num, status = records[i].split()
        h, m = hm.split(":")
        
        time = int(h)*60+int(m)
        if status == "IN":    
            in_time[car_num] = time
        else:
            parking_time = time - in_time[car_num]
            prices[car_num] += parking_time
            del in_time[car_num]
            
    for key, value in in_time.items():
        parking_time = 23*60+59 - value
        prices[key] += parking_time
    
    temp = defaultdict(int)
    for key, value in prices.items():
        if value <= fees[0]:
            temp[key] = fees[1]
        else:
            temp[key] = fees[1] + math.ceil((value-fees[0])/fees[2]) * fees[3]
            
    
    sorted_dict = sorted(temp.items(), key=lambda x : x[0])
    for _, v in sorted_dict:
        answer.append(v)
    
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees,records))