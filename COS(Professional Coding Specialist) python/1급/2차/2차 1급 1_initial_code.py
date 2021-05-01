# Book :
# * Book 은 책의 인터페이스입니다
# * 책은 get_rental_price 함수를 구현해야 합니다
# * get_rental_price 함수는 대여 기간을 매개변수로 받아 대여 요금을 계산합니다
# ComicBook :
# * ComicBook 은 만화책을 나타내는 클래스이며 , Book 인터페이스를 구현합니다
# * get_rental_price 함수는 대여 기간을 매개변수로 받아 만화책의 대여 요금을 계산합니다
# Novel :
# * Novel 은 소설책을 나타내는 클래스이며 , Book 인터페이 스를 구현합니다
# * get_rental_price 함수는 대여 기간을 매개변수로 받아 소설책의 대여 요금을 계산합니다
# 대여를
# 원하는 책들의 종류가 들어있는 리스트 book_types 와 대여 기간 day 가 매개변수로 주어질
# 때 , 전체 대여 요금을 return 하도록 solution 함수를 작성하려고 합니다 . 위의 클래스 구조를 참고하
# 여 주어진 코드의 빈칸을 적절히 채워 전체 코드를 완성해주세요

from abc import *


class Book(metaclass=ABCMeta):
    @abstractmethod
    def get_rental_price(self, day):
        pass


class ComicBook(Book):
    def get_rental_price(self,day):
        cost = 500
        day -= 2
        if day > 0:
            cost += 200*day
        return cost


class Novel(Book):
    def get_rental_price(self,day):
        cost = 1000
        day -= 3
        if day > 0:
            cost += 300*day
        return cost


def solution(book_types, day):
    books = []
    for types in book_types:
        if types == "comic":
            books.append(ComicBook())
        elif types == "novel":
            books.append(Novel())
    total_price = 0
    for book in books:
        total_price += book.get_rental_price(day)
    return total_price


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
book_types = ["comic", "comic", "novel"]
day = 4
ret = solution(book_types, day)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")