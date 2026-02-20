# * Customer:
#     * Customer : 고객을 나타내는 클래스입니다
#     * id 고객 식별 번호를 나타냅니다
#     * time : 고객이 신청한 예약 시간을 나타냅니다
#     * num_of_people : 예약 인원 수를 나타냅니다
# * Shop :
#     * Shop : 가게를 나타내는 클래스입니다
#     * reserve_list : 가게에 예약한 고객 리스트입니다
#     * reserve : 고객을 매개변수로 받아 , 예약 고객 리스트에 추가 후 true 를 return 합니다
# * HairShop :
#     * HairShop : 미용 실을 나타내는 클래스이며 , Shop 을 상속합니다
#     * reserve : 고객을 매개변수로 받아 , 미용실의 예약 기준에 맞는지 검사 합니다 . 예약을 받았다면 예
#     약 고객 리스트에 추가 후 true 를 return 하고 , 그렇지 않으면 false 를 return 합니다
# * Restaurant :
#     * Restaurant 는 레스토랑을 나타내는 클래스이며 , Shop 을 상속합니다
#     * reserve : 고객을 매개변수로 받아 , 레스토랑의 예약 기준에 맞는지 검사 합니다 . 예약을 받았다면
# 예약 고객 리스트에 추가 후 true 를 return 하고 , 그렇지 않으면 false 를 return 합니다
# 예약을 원하는 고객 정보가 담긴 리스트 customers 와 shops 가 매개변수로 주어질 때 , 두 가게에서
# 예약받은 횟수를 return 하도록 solution 함수를 작성하려고 합니다 . 위 클래스 구조를 참고하여 주어
# 진 코드의 빈칸을 적절히 채워 전체 코드를 완성해주세요

class Customer:
    def __init__(self, id, time, num_of_people):
        self.id = id
        self.time = time
        self.num_of_people = num_of_people

class Shop:
    def __init__(self):
        self.reserve_list = []
    
    def reserve(self, customer):
        self.reserve_list.append(customer)
        return True

class HairShop(Shop):
    def __init__(self):
        super().__init__()
        
    def reserve(self,customer):
        if customer.num_of_people != 1:
            return False
        for r in self.reserve_list:
            if r.time == customer.time: #r.time 이 중요
                return False
        self.reserve_list.append(customer)
        return True
    
class Restaurant(Shop):
    def __init__(self):
        super().__init__()
        
    def reserve(self,customer):
        if customer.num_of_people< 2 or customer.num_of_people >8:
            return False
        count = 0
        for r in self.reserve_list:
            if r.time == customer.time:
                count += 1
        if count >= 2:
            return False
        self.reserve_list.append(customer)
        return True
    

def solution(customers, shops):
    hairshop = HairShop()
    restaurant = Restaurant()
    
    count = 0
    for customer, shop in zip(customers, shops):
        if shop == "hairshop":
            if hairshop.reserve(Customer(customer[0], customer[1], customer[2])):
                count += 1
        elif shop == "restaurant":
            if restaurant.reserve(Customer(customer[0], customer[1], customer[2])):
                count += 1
    
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
customers = [[1000, 2, 1],[2000, 2, 4],[1234, 5, 1],[4321, 2, 1],[1111, 3, 10]]
shops = ["hairshop", "restaurant", "hairshop", "hairshop", "restaurant"]
ret = solution(customers, shops)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")