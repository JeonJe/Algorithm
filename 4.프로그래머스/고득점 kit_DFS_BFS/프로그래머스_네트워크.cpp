//https://programmers.co.kr/learn/courses/30/lessons/43162

#include <string>
#include <vector>
#include <iostream>
#include <algorithm> 
using namespace std;

const int MAX = 200;
bool visited[MAX] = { false, };

int cnt = 0; // 네트워크 수 
int N = 0;

void DFS(int v, vector<vector<int>> computers) {
	visited[v] = true; // 노드 V 방문 체크


	for (int j = 1; j < computers.size(); j++)
		if (computers[v][j] && visited[j] == false) DFS(j, computers); 
	//노드 v 와 연결된 컴퓨터중에 방문하지 않았으면 방문하기 위해 DFS 사용

}

int solution(int n, vector<vector<int>> computers) {
	int answer = 0;
	N = n;

	for (int i = 0; i < computers.size(); i++) {

		if (visited[i] == false) {  //노드 i 를 방문하지 않았으면
			DFS(i, computers);
			cnt++; // 새로운 네트워크 추가
		}
	}


	return cnt;
}

