//https://programmers.co.kr/learn/courses/30/lessons/42885

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
	int pair = 0;

	int heavy = people.size()-1;
	int light = 0; 
	int weight = limit;

	sort(people.begin(), people.end()); // 오름 차순으로 정렬

	while (light < heavy) { 

		if (people[light] + people[heavy] <= limit) { //사람을 태울 수 있을 경우
			light++;
			heavy--;
			pair++; // 두 사람이 함께 타는 경우 
		}
		else  //가장 무거운 사람때문에 한 번에 태울 수 없을 경우 
			heavy--; // 가장 무거운 사람은 혼자 탐.
		
	}
	
	return people.size()- pair; // 4명 중 2명이 짝이라면 pair는 1, 즉 4-1인 3개의 보트
}

int main() {

	vector<int>people{ 70, 50,80, 50 };
	cout << solution(people, 100);
	return  0;
}