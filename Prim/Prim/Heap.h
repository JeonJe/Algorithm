#pragma once
#include <vector>
#include <utility>
#include <iostream>
using namespace std;

class HeapSort
{
private:
	vector<pair<int,int>> v;

public:
	HeapSort();
	HeapSort(vector<pair<int,int>> v);
	~HeapSort();

	void print_heap();	//heap을 출력하는 함수
	void min_heapfity(int i);	//heap을 min heap성질을 만족하게 만들어주는 함수
	void build_heap();		// heap 을 구성시키는 함수
	void heapSort();
	void vector_swap( int a , int b);
	void update(int to, int weight);
	bool search(int a);
	vector<pair<int, int>> extract_min();
	bool IsEmpty();
	int getKey(int vertex);  //입력한 vertex의 key값을 가져오는 함수
};