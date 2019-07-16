
#include "Heap.h"

HeapSort::HeapSort()	// 생성자 
{

}
HeapSort::HeapSort(vector<pair<int, int>>  V) // 오버로드 된 생성자
{
	v = V; // 파라미터로 들어온 V를 v에 set
}

HeapSort::~HeapSort()	//소멸자
{
	v.clear();
}

bool HeapSort::IsEmpty()	//Heap이 비어있는지 확인하는 함수 
{
	if (v.size() == 0) return true;	//vector 의 원소가 0이면 true
	else	return false;	//아니면 false
}

vector<pair<int, int>>  HeapSort::extract_min()	//최소의 key값을 가지고 있는 vertex를 가져오는 함수
{
	vector<pair<int, int>> min; //최소의 key값을 가지는 vertex를 담을 변수
	int i;
	i = v.size() - 1;//	i 는 size - 1;

	if (i < 0) {  //size가 0이였으면 예외처리
		cout << "Heap is empty" << endl;
		return min;
	}

	vector_swap(0, i);	// 0번째 vector (최솟값) 와 마지막 vector 원소 swap
	min.push_back(make_pair(v[v.size() - 1].first, v[v.size() - 1].second));
	v.pop_back();			//min vector에 최소값을 가지는 vertex 번호와, 가중치 담음
							//v에서 원소의 가장 뒤부분을 pop
	min_heapfity(0);		// root 부터 다시 heapfity
	return min;				//최소의 key값을 가지는 vertex 반환

}

void HeapSort::update(int to, int weight)
{
	for (size_t i = 0; i < v.size(); i++)
	{
		if (v[i].first == to)  //Q에 남아있는 V인지 체크
		{
			v[i].second = weight; // 파라미터로 들어온 가중치로 vertex 가중치 업데이트
		}
	}
	build_heap();	// 가중치가 바뀌었으므로 다시 정렬 

}
bool HeapSort::search(int to_vertex)  //인자로 Q안에서 찾고자하는 vertex 번호 입력
{
	for (size_t i = 0; i < v.size(); i++) //Q 에 남아있는 vertex를 체크
	{
		if (v[i].first == to_vertex)	//인자로 들어온 vertex번호와 Q의 vertex번호가 같다면
		{
			return true;	//Q에 존재하는 vertex, true 리턴
		}
	}
	return false;	//Q에 없는 vertex이므로 false return
}

int HeapSort::getKey(int vertex) //입력한 vertex의 key값을 가져오는 함수
{
	int a = 0;
	for (size_t i = 0; i < v.size(); i++)  //Q 에 남아있는 vertex를 체크
	{
		if (v[i].first == vertex) //인자로 들어온 vertex번호와 Q의 vertex번호가 같다면
		{
			a = v[i].second; //key값을 리턴.
			return a;
		}
	}
	return -1;	//Q에 존재하지 않은 vertex라면 -1 리턴
}


void HeapSort::print_heap()	//heap을 출력하는 함수
{
	for (size_t i = 0; i < v.size(); i++)
		cout << "first = " << v[i].first << " second = " << v[i].second << endl;
	cout << endl;
}


void HeapSort::min_heapfity(int i)	//heap을 min heap성질을 만족하게 만들어주는 함수
{
	size_t  l, r;
	int smallest;
	l = 2 * i;		//왼쪽 자식 노드
	r = (2 * i + 1);	//오른쪽 자식 노드
	if ((l < v.size()) && v[l].second < v[i].second) smallest = l;
	else smallest = i;		//l 이 벡터 사이즈 내에 존재하고, 왼쪽자식 노드의 key값이 
							//부모노드  key값보다 작으면 smallest 는 l 아니면 i 

	if ((r < v.size()) && (v[r].second < v[smallest].second)) smallest = r;
	//r 이 벡터 사이즈 내에 존재하고, 오른쪽 자식 노드의 key값이 smallest 값보다
	//작으면 smallest 는 r
	if (smallest != i)	// 부모가 가장 작은게 아니라면
	{
		vector_swap(i, smallest);	//부모와 가장 작은 노드 교환
		min_heapfity(smallest);		//smallest 를 부모로해서 min heap 성질만족시키는 heap 구성
	}
}


void HeapSort::build_heap()		// heap 을 구성시키는 함수
{
	for (int i = (v.size() / 2); i >= 0; i--) 	min_heapfity(i);
	// min_heapfity를 호출하여 힙의 성질을 갖게 구성
}

void HeapSort::vector_swap(int a, int b)	//a,b 인덱스의 vector를 swap하는 함수
{
	pair<int, int> temp;
	temp = v[a];
	v[a] = v[b];
	v[b] = temp;
}

void HeapSort::heapSort()	//우선순위 Queue 를 min heap을 사용하여 정렬하는 함수
{
	build_heap();

}
