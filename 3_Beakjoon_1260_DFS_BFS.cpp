#include <iostream>
#include <algorithm> //sort
#include <vector>
#include <stack>
#include <queue>
#include <cstring> //memset
using namespace std;

int N;				// ������ ����
int M;				// ������ ����
int V;				 // Ž���� ������ ��ȣ
vector<int> ad[1001]; // ���� ����Ʈ
bool visit[1001];		//���� �湮 Ȯ��

void BFS()
{
	memset(visit, 0, sizeof(visit));
	queue<int> q;	// ť ����
	q.push(V);

	while (!q.empty())
	{
		int v = q.front();
		q.pop();
		if (!visit[v])	//�湮���� �ʾ����� �湮
		{
			cout << v << " ";
			visit[v] = true;
		}
		for (int j = 0; j < ad[v].size();j++)
		{
			if (!visit[ad[v].at(j)]) //�ֺ� vertex �湮 ����Ȯ��
				q.push(ad[v].at(j));

		}
	}

}

void DFS()
{
	memset(visit, 0, sizeof(visit));  //size
	stack<int> s;	//���� ����
	s.push(V);

	while (!s.empty())
	{
		int v = s.top();
		s.pop();
		if (!visit[v]) 	//�湮���� �ʾ����� �湮
		{
			cout << v << " ";
			visit[v] = true;
		}

		for (int j = ad[v].size() - 1; j >= 0;j--)
		{
			if (!visit[ad[v].at(j)]) //�ֺ� vertex �湮 ����Ȯ��
				s.push(ad[v].at(j));
		}
	}
}

int main()
{

	cin >> N >> M >> V;

	for (int i = 1; i < M + 1; i++)
	{
		int start, end;
		cin >> start >> end;
		ad[start].push_back(end);	//������
		ad[end].push_back(start);
	}
	for (int j = 1; j < N + 1; j++)	//���� ��ȣ�� ���� �ͺ��� �湮
	{
		sort(ad[j].begin(), ad[j].end());
	}

	DFS();
	cout << endl;
	BFS();
	return 0;

}
