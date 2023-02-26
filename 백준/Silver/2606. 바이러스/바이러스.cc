#include<iostream>
#include <vector>
#include <cstring>
#include<stack>
using namespace std;

vector <int> ad[101];
bool visit[101];
int C;	//바이러스에 감염된 컴퓨터 수 
int N, P;
// N은 컴퓨터의 수 , P 는 네트워크 상에서 직접연결되어 있는 컴퓨터 쌍의 수 

void DFS()
{
	int V = 1;
	C = 0;
	memset(visit, false, sizeof(visit));
	stack<int> s;
	s.push(V);

	while (!s.empty())
	{
		V = s.top();
		s.pop();
		if (!visit[V])
		{
			C++;
			visit[V] = true;
		}
		for (int i = 0;i < ad[V].size();i++)
		{
			if (!visit[ad[V].at(i)])
				s.push(ad[V].at(i));
		}
		
	}
}


int main()
{
	
	cin >> N >> P;
	int start, end;

	for (int i = 1; i <= P; i++) // 페어의 수만큼 반복문 
	{
		cin >> start >> end;
		ad[start].push_back(end);
		ad[end].push_back(start);
	}
	DFS();
	cout << C-1 << endl;



}