def truckTour(petrolpumps):
    # Write your code here
    length = len(petrolpumps)
    answer = 0
    petrol = 0
    for i in range(length):
        #연료 - 다음 주유소까지 거리 = 남은 연료를 petrol에 더함
        petrol += petrolpumps[i][0] - petrolpumps[i][1]
        if petrol < 0:
            petrol = 0
            answer = i+1
    return answer



petro = [[1,5],[10,3],[3,4]]

print(truckTour(petro))