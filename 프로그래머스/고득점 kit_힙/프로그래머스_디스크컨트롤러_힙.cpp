
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool cmp(pair<int, int>a, pair<int, int>b) {
	if (a.first == b.first) return a.second < b.second;
	//작업 소요시간이 같다면 먼저 요청된것부터
	else return a.first < b.first;
	//작업 소요시간이 작은 순서부터
}

// 왼쪽이 오른쪽보다 작을 수 있도록 정렬 
int solution(vector<vector<int>> jobs) { //작업이 요청되는 시점,소요되는 시간

	int nsize = jobs.size(); // 몇개의 작업이 요청되었는지
	int workTime = 0;

	vector<pair<int, int>> v; //작업이 소요되는시간, 작업이 요청되는 시점

	for (int i = 0; i < nsize; ++i)
		v.push_back({ jobs[i][1],jobs[i][0] });

	sort(v.begin(), v.end(), cmp);

	int cur_time = 0, total_time = 0;

	while (!v.size() == 0) { // 작업요청이 존재하면
		for (int i = 0; i < v.size(); ++i) { // 작업요청들을 확인
			if (cur_time >= v[i].second) { //현재 시간이 작업요청시간과 같거나 지난경우
				cur_time += v[i].first;			// 작업 소요시간 추가
				total_time = total_time + cur_time - v[i].second;
									// 작업이 요청된시점을 빼줘야함
				v.erase(v.begin() + i); //해당요청이 수행되었으므로 삭제
				break;
			}
			if (i == v.size() - 1) cur_time++;
									//현재 작업이 끝나고 다음 수행작업까지 공백이 있을 경우
		}
	}

	return total_time / nsize;
}

int main()
{
	vector<vector<int>> jobs = { {0,3},{1,9},{2,6} };
	cout << solution(jobs);
	return 0;
}