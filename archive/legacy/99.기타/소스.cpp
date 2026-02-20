#include <iostream>
#include <queue>

using namespace std;

int main(void) {
	int a;
	int b;
	int message_t = 0;
	int time = 1;
	int check = 0;

	queue<int> q;

	bool working[11] = { false, }; //컨슈머들
	int working_time[11] = { 0, }; //남은 일 시간

	cin >> a >> b;   //a 는 메세지 수 , b는 컨슈머 수

	for (int i = 0; i < a; i++) {   //메세지를 큐에 넣음
		cin >> message_t;
		q.push(message_t);
	}

	while (1) {                  //컨슈머가 일을 하고 있을 동안
		check = 0;

		for (int i = 0; i < b; i++) {     // 컨슈머들

			if (working[i] == false && q.size() > 0) {      // 컨슈머가 일을 하고 있지 않으면
				working[i] = true;
				working_time[i] = q.front();  // 일을 가져감
				q.pop();
			}

			if (working[i] == true) { // 컨슈머가 일을 하고 있으면
				working_time[i]--;  //시간 감소
				if (working_time[i] == 0) working[i] = false; // 0이 되면 다음 일 받을 준비
			}

			if (working[i] == false)   // 일하지 않은 컨슈머 체크
				check++;

		}

		if (check == b) { // 모두 일안하고 있으면 끝
			break;
		}

		time++;
	}



	cout << time << endl;
	return 0;
}