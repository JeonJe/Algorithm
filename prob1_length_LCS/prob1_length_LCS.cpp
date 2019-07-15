#include <iostream>
#include <string.h>
using namespace std;
void print(int** table, int i, int j);
void print(char** table, int i, int j);		//bottom-up table 출력하기 위한 함수

int main()
{
	char X[] = "GOODMORNING";	//문자열 X
	char Y[] = "GUTENMORGEN";	//문자열 Y
	int m = sizeof(X) / sizeof(char);   // X 문자배열의 길이
	int n = sizeof(Y) / sizeof(char);	// Y 문자배열의 길이

	char *x = new char[m + 1];
	char *y = new char[n + 1];
	x[0] = ' '; for (int i = 1; i < m + 1;i++) 	x[i] = X[i - 1]; // bottom-up table 생성을 위해 맨앞에 공백 삽입
	y[0] = ' '; for (int i = 1; i < n + 1;i++) 	y[i] = Y[i - 1];

	char **b = new char*[n + 1];
	int **c = new int*[n + 1];
	for (int i = 0; i < n + 1;i++)
	{
		b[i] = new char[m + 1];   //역추적으로 LCS 문자열을 찾기 위한 배열 b
	    c[i] = new int[m + 1];	  //LCS의 길이 정보를 담고 있는 배열 c
	}

	for (int i = 0; i < n + 1;i++)		//b,c 배열 초기화
	{
		for (int j = 0; j < m + 1;j++)
		{
			b[i][j] = '_';
			c[i][j] = 0;
		}
	}

	for (int i = 1; i < n;i++)	// Y 배열의 문자들에 대한 반복문
	{
		for (int j = 1; j < m; j++)	// X 배열의 문자들에 대한 반복문
		{
			if (y[i] == x[j])  // X와 Y 배열의 글자가 같다면
			{
				c[i][j] = c[i - 1][j - 1] + 1; // X와 Y가 같은 위치의 c배열의 인덱스값 1증가
				b[i][j] = 'W';	// 역추적을 위해 W (↖) 표시 
			}
			else if (c[i - 1][j] >= c[i][j - 1])	//X와 Y 문자 위치 위쪽방향 배열의 값이 이 왼쪽방향 보다 크면
			{
				c[i][j] = c[i - 1][j];	//X,Y 좌표 의 인덱스를 위쪽 값으로(이전까지 최대 LCS 길이) 로 설정
				b[i][j] = 'U';		     //위쪽 방향이 큼을 U(↑)로 표시 
			}
			else
			{
				c[i][j] = c[i][j - 1];	//아니라면 X,Y 좌표 의 인덱스를 왼쪽 값으로(이전까지 최대 LCS 길이) 로 설정
				b[i][j] = 'L';		     //왼쪽 방향이 큼을 U(←)로 표시 
			}
		}
	}
	print(c, m, n);		//LCS 최대 길이 정보 를 담은 table 출력
	print(b, m, n);		//역추적을 위한 표시를 담은 table 출력 

	cout << "X : " << X << endl << "Y : " << Y << endl; // X,Y 배열 출력
	cout << "LCS의 길이 : "<<c[n-1][m-1]<<endl; //LCS 길이 출력

	delete x;
	delete y;
	for (int i = 0; i < n + 1;i++)delete[] b[i];   //동적 할당 배열들 해제
	delete[] b;
	for (int i = 0; i < n + 1;i++) delete[] c[i];
	delete[] c;

	return 0;

}

void print(int** table, int i, int j)	//LCS 최대 길이 정보 를 담은 table 출력
{
	for (int a = 0; a < j;a++)
	{
		for (int b = 0; b < i;b++)
		{
			cout << table[a][b] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

void print(char** table, int i, int j)		//역추적을 위한 표시를 담은 table 출력
{
	for (int a = 0; a < j;a++)
	{
		for (int b = 0; b < i;b++)
		{
			cout << table[a][b] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

