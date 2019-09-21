#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(int stock, vector<int> dates, vector<int> supplies, int k) {
	int answer = 0;
	priority_queue<int> pq;
	int lastDate = 0;

	while (stock < k) {      //st가 k보다 같거나 커지면 공장을 가동 못함 ( st는 하루마다 -1 )
		while (lastDate < dates.size() && dates[lastDate] <= stock)
			// lastDate가 date의 사이즈 보다 작고 (인덱싱 범위)
			// 추가하려는 날 보다 stock이 작으면 ( 버틸 수 없으면)  
			pq.push(supplies[lastDate++]); // 최대 공급량을 큐에 넣고 +1증가

		stock += pq.top(); // 가장 많은 공급량을 꺼내서 추가
		pq.pop();
		answer++;       // 해외 공장에서 수입 횟수 증가 
	}

	return answer;
}