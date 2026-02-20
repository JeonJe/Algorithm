#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <queue>
#include <cstring>
#include <stdio.h>

using namespace std;
int N, M;

int map[1001][1001];
int cache[1001][1001][2];  //���⼭ ���� �ո� ����, �ִ� ��ΰ� �� �������� Ȯ�ΰ���

int Dx[] = { 0,0,-1,1 };
int Dy[] = { -1,1,0,0 };
int solve() {

	queue<pair<int, pair<int, int>>> q; // �� ���� Ƚ��,  y, x
	q.push({ 1, { 0,0 } }); // 1�� ���� ��ȸ�� �ִ� 0,0 ���� ����
	cache[0][0][1] = 1;

	while (!q.empty()) {
		int bw = q.front().first; // ���� �μ� ��ȸ
		int y = q.front().second.first;
		int x = q.front().second.second;

		q.pop();

		if (0 > y || N <= y || 0 > x || M <= x) continue; //���� ���̸� �ݺ�������
		if (y == N - 1 && x == M - 1) return cache[y][x][bw]; // y�� x ���� �����ϴ� �ִ�  Ƚ��

		for (int i = 0; i < 4; ++i) {
			int new_y = y + Dy[i];  //4 �������� Ȯ��
			int new_x = x + Dx[i];

			if (0 <= new_y && new_y < N && 0 <= new_x && new_x < M) {  //���� ���� ���̸鼭
				if (map[new_y][new_x] == 0 && cache[new_y][new_x][bw] == 0) { // ���� ����, �湮���������� 
					cache[new_y][new_x][bw] = cache[y][x][bw] + 1; // y,x �� ���� ����� �� + 1, ���� �μ� ��ȸ�� �״�� ������
					q.push({ bw, { new_y, new_x } });
				}
				if (map[new_y][new_x] == 1 && bw == 1) { // ���� ������ ���� �����ְ�, ���� ��ȸ�� �ִٸ� 
					cache[new_y][new_x][bw - 1] = cache[y][x][bw] + 1; // y,x �� ���� ����Ǽ� + 1, ������ ���� �μ� ��ȸ�� 0���� ����
					q.push({ bw - 1 , { new_y, new_x } });
				}
			}
		}
	}

	return -1;

}
int main()
{
	cin >> N >> M; // N �� row �� �� (����) , M�� col�� �� (����)

	memset(map, 0, sizeof(map));
	memset(cache, 0, sizeof(cache));

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j)
			scanf("%1d", &map[i][j]);
	}


	cout << solve();
	return 0;

}