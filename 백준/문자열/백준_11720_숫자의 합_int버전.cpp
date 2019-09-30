#include <stdio.h>

int main() {
	int N=0;
	int num=0;
	long long sum=0;
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {

		scanf("%1d", &num);;
		sum += num;
	}

	printf("%d\n", sum);
	return 0;
}