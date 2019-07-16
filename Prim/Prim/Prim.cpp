#include <stdio.h>
#include <limits.h>
#include <time.h>
#include <iostream>
#include <vector>
#include <utility>
#include "Heap.h"

using namespace std;
#define matrix_size 8 // adjacency-matrix 의 크기 

void getAdj(int graph[matrix_size][matrix_size], int vertex, vector<pair<int, int>>* m); //입력 vertex 주변 노드를 얻는 함수
void Prim(int graph[matrix_size][matrix_size]); // MST를 구하는 프림 알고리즘 


int main()
{
	/*int graph[matrix_size][matrix_size] = { { 0,6,12,0,0,0,0 },
											{ 6,0,5,0,14,0,0,8 },
											{ 12,5,0,9,0,7,0,0 },
											{ 0,0,9,0,0,0,0,0 },
											{ 0,14,0,0,0,0,0,3 },
											{ 0,0,7,0,0,0,15,10},
											{ 0,0,0,0,0,15,0,0},
											{ 0,8,0,0,3,10,0,0} };*/
/*int graph[matrix_size][matrix_size] = { {0,12,INT_MAX,INT_MAX,5 },
											{12,0,3,INT_MAX,INT_MAX },
											{INT_MAX ,3,0,4,8},
											{ INT_MAX ,INT_MAX ,4,0,INT_MAX },
											{ 5,INT_MAX ,8,INT_MAX ,0}	};*/
	int graph[matrix_size][matrix_size] = { {0,7,0,0,0,10,15,0},
											{7,0,12,5,0,0,0,9}, //1}
											{0,12,0,6,0,0,0,0}, //2
											{0,5,6,0,14,8,0,0},//3
											{0,0,0,14,0,3,0,0}, //4
											{10,0,0,8,3,0,0,0}, //5
											{15,0,0,0,0,0,0,0}, //6
											{0,9,0,0,0,0,0,0}, //7
	};

	Prim(graph);		//graph의 MST를 구하기위해 Prim 함수 호출
	return 0;
}

void getAdj(int graph[matrix_size][matrix_size], int vertex, vector<pair<int, int>>* m) //graph와 vertex, 주변노드 정보를 담을 m
{
	for (int i = 0; i < matrix_size;i++)	//adjacency-matrix의 크기만큼 탐색하면서
	{
		if (graph[vertex][i] != 0)	//vertex로부터 연결된 vertex (가중치가 존재) 가 있는 지 확인
			m->push_back(make_pair(i, graph[vertex][i])); // 존재하면 m 에 어느 vertex 인지, 가중치와 함께 vector에 입력 
	}
}

void Prim(int graph[matrix_size][matrix_size])  // 인접행렬을 사용해서 MST을 구하는 Prim's algorithm
{
	int MST[matrix_size] = { 0 }; // MST 정보를 담을 배열 MST

	vector<pair<int, int>> Q;	//Vertex 정보를 가지고 있는 vector Q

	for (int i = 0; i < matrix_size;i++) Q.push_back(make_pair(i, INT_MAX));	//각 vertex 의 key값을 MAX로설정

	srand(time(NULL));
	int s = (rand() % Q.size() - 1) + 1;	//임의의 시작점 s 
	Q.at(s).second = 0; // 시작점의 key값에 0 입력

	HeapSort PriorityQueue(Q);	//vector Q를 가지고 우선순위 큐 생성
	PriorityQueue.heapSort();	//key값에 따른 min_heap 정렬 

	while (!(PriorityQueue.IsEmpty()))	//우선순위 큐에 값이 존재할동안
	{
		vector<pair<int, int>> u = PriorityQueue.extract_min();	// 우선순위 큐에서 key값이 최소인 vertex를 큐에서 빼서 u로 assign
		cout << "\nextract_min from Q : " << "u = " << u[0].first << " weight = " << u[0].second << endl;
		cout << endl;		// Queue 에서 가져온 최솟값 출력

		vector<pair<int, int>> adjacency;	//주변 vertex 를 담을 벡터 선언
		getAdj(graph, u[0].first, &adjacency);   //그래프에서 u에 주변 vertex를  adjacency 에 담아옴

		for (size_t i = 0; i < adjacency.size(); i++)		// 근접노드들 을 탐색 
		{
			int v = adjacency[i].first;		// v 는 주변 vertex의 번호 
			cout << "====== 주변 vertex " << v << " ======" << endl;
			if (PriorityQueue.search(v)		 // PriorityQueue에서 주변노드 v가 Q에 있는지 확인 
				&& (graph[u[0].first][v] < PriorityQueue.getKey(v))) // w(u,v) < key[v] 일 경우
			{
				cout << " vertex " << v << " key : " << PriorityQueue.getKey(v)
					<< " update to " << graph[u[0].first][v] << endl; // update 된 키값 출력
				MST[v] = u[0].first;							//MST[V] 에 이전 노드인 u 기록
				PriorityQueue.update(v, graph[u[0].first][v]); //  w(u,v)로 key[v] update

			}
			else
				cout << " vertex " << v << " key : " << PriorityQueue.getKey(v) << endl;
								// 업데이트 되지 않은 키값 출력, key값이 -1 일 경우는 방문했던 노드 표시
		}
		adjacency.clear();	//주변vertex를 담고있는 vector 초기화
		u.clear();		// 최소 key값을 가진 vertex 초기화
	}

	cout << "======= MST =======" << endl << endl;
	for (int i = 0; i < matrix_size;i++)
	{
		if (graph[i][MST[i]] != 0 && graph[i][MST[i]] != INT_MAX)	//MST 출력, 가중치가 INT_MAX이거나,0 일경우는 제외
			cout << " V : " << MST[i] << " -> " << i << " weight : " << graph[i][MST[i]] << endl;
	}
	cout << endl;
	return;
}

