#include <iostream>
#include <cstring>
#include <queue>


using namespace std;

/*문제
연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다.이 게임은 브라운이 코니를 잡거나,
코니가 너무 멀리 달아나면 끝난다.게임이 끝나는데 걸리는 최소 시간을 구하시오.

조건
코니는 처음 위치 C에서 1초 후 1만큼 움직이고, 이후에는 가속이 붙어 매 초마다 
이전 이동 거리 + 1만큼 움직인다.즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.

브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
코니와 브라운의 위치 p는 조건 0 <= x <= 200, 000을 만족한다.
브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다.*/

int C, B;

int solve(int conyPosition, int brownPosition) {
	
	int time = 0;
	bool brown_visit[200001][2];
	memset(brown_visit, false, sizeof(brown_visit));
	queue<pair<int, int>> queue;

	queue.push(make_pair(brownPosition, 0)); // 0초에 브라운 위치

	while (1) {

		conyPosition += time;

		if (conyPosition > 200000) return -1;	//코니가 범위를 벗어나면 게임 끝
		if (brown_visit[conyPosition][time % 2]) return time;	// 브라운이 코니의 위치와 같다면 ( 홀수, 짝수 )

		/*t초에서 위치가 p일 때 t + 1초에서는 위치가 p일수는 없지만 t + 2 초에서는 위치가 p일수 있다
		방문시간을 홀수, 짝수로 나누어 고려,t값을 증가시키면서 코니가 t초 후에 p 위치라면 브라운이 p위치에 t - 2k(k >= 0) 시간에 도착했는지 여부를 판단*/
		int current_queue_size = queue.size();
		for (int i = 0; i < current_queue_size; i++) {     // 브라운이 갈 수 있는 경우들에 대해 확인
			int current_brownPosition = queue.front().first; // 현재 브라운 위치 
			int current_time = queue.front().second;		// 현재 시간
			queue.pop();

			int new_time = (current_time + 1) % 2;		//현재 시간이 홀수 인지 짝수 인지 확인
			int new_brownPosition;

			cout << conyPosition << " " << current_brownPosition << endl;
			new_brownPosition = current_brownPosition + 1;		//브라운 이동
			if (new_brownPosition <= 200000 && brown_visit[new_brownPosition][new_time] == false) {
				brown_visit[new_brownPosition][new_time] = true;
				queue.push(make_pair(new_brownPosition, new_time));
			}

			new_brownPosition = current_brownPosition - 1;		//브라운 이동
			if (new_brownPosition > 0 && brown_visit[new_brownPosition][new_time] == false) {
				brown_visit[new_brownPosition][new_time] = true;
				queue.push(make_pair(new_brownPosition, new_time));
			}

			new_brownPosition = current_brownPosition *2 ;		//브라운 이동
			if (new_brownPosition <= 200000 && brown_visit[new_brownPosition][new_time] == false) {
				brown_visit[new_brownPosition][new_time] = true;
				queue.push(make_pair(new_brownPosition, new_time));
			}

		}  //end of for statement
		time++;
	}
}
int main() {
	C = 6;
	B = 3;
	int result = solve(C, B);
	cout << result << endl;
	return 0;
}

/*
입력: 11 2
출력 : 5

코니의 위치 : 11 → 12 → 14 → 17 → 21 → 26
브라운의 위치 : 2 → 3 → 6 → 12 → 13 → 26

C = 11, B = 1인 경우
하지만 실제로는 1 → 2 → 3 → 4 → 8 → 16 → 32로 이동하여 6초 만에도 잡을 수 있습니다.

C = 6, B = 3인 경우
절대로 3초 만에 잡을 수 없고 3 → 6 → 7 → 8 → 16로 이동하여 4초에 최초로 잡을 수 있습니다
*/