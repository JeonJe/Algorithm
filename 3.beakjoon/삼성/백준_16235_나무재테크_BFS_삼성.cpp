//https://www.acmicpc.net/problem/16235

#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

struct TREE{
	int y, x, age;

};

bool cmp(TREE& a, TREE&b) {
	return (a.age < b.age); // 나무의 나이거 어린순으로 정렬
	//초기 나무 입력의 정렬에 사용
}

struct QUEUE {
	int f, b; //front, back
	TREE tree[684000];

	QUEUE() {
		init();
	}
	void init() {
		f = 0;
		b = 0;
	}
	bool isempty() {
		return (f == b); 
	}
	void push(TREE val) {
		tree[b++] = val; // 맨뒤에 추가하고 b 증가
	}
	void pop() {
		++f;
	}
	TREE front() {
		return tree[f];
	}
	int size() {
		return (b - f);
	}

};
const int MAX = 100;

int n, m, k;
QUEUE tree[2];

TREE init_tree[100]; //초기 입력받는 트리
QUEUE new_tree; //초기에는 아무것도 없고 번식하게 되면 여기에 들어옴
QUEUE dead_tree, birth_of_child_tree; // 올해 죽은 나무의 큐와 번식이 가능한 나무의 큐

int map[10][10], add[10][10];
//양분을 저장할 map 배열 , 추가적인 양분을 저장할 add 배열
int main() {

	cin >> n >> m >> k;    

	//N X N
	//m개 줄에는 심은 나무의 정보를 나타내는 x,y,z (x,y)는 위치 z는 나이
	//k 는 몇년 후에도 살아있는지 

	for (int y = 0; y < n; ++y) {
		for (int x = 0; x < n; ++x) {
			cin >> add[y][x];
			map[y][x] = 5;

		}
	}
	for (int i = 0; i < m; ++i) { //초기 나무 정보 입력
		cin >> init_tree[i].y >> init_tree[i].x >> init_tree[i].age;
		init_tree[i].y--, init_tree[i].x--; // 배열을 0부터 사용하기 때문에 하나 줄임
	}

	sort(init_tree, init_tree + m, cmp); //나무의 나이가 작은것부터 큰것까지
	
	int cur = 0, next = 0;
	for (int i = 0; i < m; ++i) {
		tree[cur].push(init_tree[i]); //cur 트리에는 나이가 어린 나무부터 저장 
	}

	

	for (int i = 0; i < k; ++i) { // 0부터 k년까지

		next = (cur + 1) % 2; // 현재가 0 이면 next는 1
						     // next가 현재가 되면 cur 는 1, next는 0이 됨
							 //배열 2개로 올해, 내년을 나누기 위해 사용
		
		dead_tree.init();
		birth_of_child_tree.init(); // main 에서 큐를 정의하면 stack에 쌓이므로 큰 배열로 잡지못함
		tree[next].init();			//글로벌에서 정의하여 힙을 사용해야함 

		while (!new_tree.isempty()) { //어린 나무부터 양분흡수
			TREE cur_tree = new_tree.front(); new_tree.pop();

			if (map[cur_tree.y][cur_tree.x] >= cur_tree.age) { //살아 남을 수 있는 트리, 나이보다 양분이 많음 
				map[cur_tree.y][cur_tree.x] -= cur_tree.age; //양분을 흡수했으므로 업데이트

				++cur_tree.age; //내년으로 가기전에 나이를 한살올림
				tree[next].push(cur_tree); //넥스트 트리에 넣음 (다음년도에 사용하는 나무)

			}
			else 
				dead_tree.push(cur_tree); // 양분흡수 못했으므로 죽은 나무 큐에 삽입

			
		}

		while (!tree[cur].isempty()) { //기존에 살아있는 나무 양분흡수
			TREE cur_tree = tree[cur].front(); tree[cur].pop();

			if (map[cur_tree.y][cur_tree.x] >= cur_tree.age) { //살아 남을 수 있는 트리, 나이보다 양분이 많음 
				map[cur_tree.y][cur_tree.x] -= cur_tree.age; //양분 흡수

				++cur_tree.age; //내년으로 가기전에 나이를 한살올림
				tree[next].push(cur_tree); //넥스트 트리에 넣음

				if ((cur_tree.age % 5) == 0)   //번식이 가능한 트리, 나이가 5의 배수인 나무는 번식 가능한 나무 큐에 추가
					birth_of_child_tree.push(cur_tree);				

			}
			else 
				dead_tree.push(cur_tree); // 양분흡수 못했으므로 죽은 나무 

			
		}

		while (!dead_tree.isempty()) { //여름에 할일, 죽은 나무만 확인
			TREE cur_tree = dead_tree.front(); dead_tree.pop();
			map[cur_tree.y][cur_tree.x] += (cur_tree.age / 2); // 나무가 있던 칸에 양분으로 추가
		}

		const int dy[] = { -1,-1,-1,0,0,+1,+1,+1 };
		const int dx[] = { -1,0,+1,-1,+1,-1,0,+1 };  //팔방향

		new_tree.init(); // 사용하기 전에 초기화 한번
		while (!birth_of_child_tree.isempty()) { //가을이 되면 번식
			TREE cur_tree = birth_of_child_tree.front(); birth_of_child_tree.pop(); //번식 가능한 나무들
			for (int dir = 0; dir < 8; ++dir) {  //8방향으로
				TREE next_tree;  
				next_tree.y = cur_tree.y + dy[dir];
				next_tree.x = cur_tree.x + dx[dir];
				next_tree.age = 1;  //1살짜리 나무 

				if (next_tree.y < 0 || next_tree.y >= n || next_tree.x < 0 || next_tree.x >= n) continue;

				new_tree.push(next_tree); //한 살짜리 나무 번식(새로운 나무 큐에 삽입)
			}
		}

		for (int y = 0; y < n; ++y) { //겨울에 할 일 
			for (int x = 0; x < n; ++x) {
				map[y][x] += add[y][x]; //입력받은 양분 추가
			}
		}

		cur = next; // 해가 바뀌었으므로 현재 queue에는 내년이 들어감


	}
	cout << tree[next].size() + new_tree.size() << endl;
	
	return 0;

}