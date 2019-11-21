//https://programmers.co.kr/learn/courses/30/lessons/42629
#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(int stock, vector<int> dates, vector<int> supplies, int k) {
	int answer = 0;
	priority_queue<int> pq;
	int lastDate = 0; // 최대한 버티다가 마지막으로 공급받는 날

	while (stock < k) {      //st가 k보다 같거나 커지면 공장을 고려할 필요 없음
		while (lastDate < dates.size() && dates[lastDate] <= stock)
			// lastDate가 date의 사이즈 보다 작고 (인덱싱 범위)
			// 마지막 공급날이  남은 stock이 작으면 ( 아직 버틸 수 있으면 )  
			pq.push(supplies[lastDate++]); // 일단 최대 공급량을 큐에 넣고 lastDate를+1증가
		
		//while 을 빠져나옴 -> 현재남은 stock 으로 버틸 수 없고 공급받아야하는 경우
		stock += pq.top(); //큐에서 가장 많은 공급량을 꺼내서 추가
		pq.pop();
		answer++;       // 해외 공장에서 수입 횟수 증가 
	}

	return answer;
}
