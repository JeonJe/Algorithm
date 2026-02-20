//https://www.acmicpc.net/problem/15686 

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct position {
	int y, x;
};

int n, m, type, ret;
vector<position> house, shop, pick;

void dfs(int pos) {
	if (pick.size() == m) { //m 개의 치킨집이 선택되었다면

		int candi = 0; // 가장 최소값의 합 

		for (int i = 0; i < house.size(); ++i) { //집 
			int min_dist = 1000000; // 가장 최소 값을 구하기 위해 사용
			for (int j = 0; j < pick.size(); ++j) { //치킨집
				min_dist = min(min_dist,     //각 집마다 가장 가까운 치킨집과의 거리의 합이 최소가 되는 값만 갱신
					abs(house[i].y - pick[j].y) + abs(house[i].x - pick[j].x));
			}
			candi += min_dist;  // 0 번째 집에서 가장 작은 값 + 1번째 집에서 가장 작은값 + ...
		}

		if (ret > candi)
			ret = candi;

		return;
	}

	for (int i = pos; i < shop.size(); ++i) {
		pick.push_back(shop[i]); //넣고 
		dfs(i + 1);  //돌리고 
		pick.pop_back(); // 확인했으면 빼기 
	}
}

int main() {


	cin >> n >> m;

	position target;
	for (int y = 0; y < n; ++y) {
		for (int x = 0; x < n; ++x) {
			cin >> type;
			if (type == 1) {
				target.y = y; target.x = x;
				house.push_back(target);

			}
			else if (type == 2) {
				target.y = y; target.x = x;
				shop.push_back(target);

			}
		}
	}
	ret = 999999;
	dfs(0);
	cout << ret;
	return 0;
}