# 그래프의 노드 수와 노드 연결 순서가 주어질 때 , 몇 번째 연결에 사이클이 생기는지 알고 싶습니다 .
# 예를 들어 , 노드가 3 개이고 노드를 [[1, 2], [1, 3], [2, 3]] 순으로 연결한다면 아래 그림과 같습니다
# 그래프의 노드 수 n, 노드 연결 순서 connections 가 매개변수로 주어질 때 , 몇 번째 연결에 사이클이
# 생기는지 return 하도록 solution 함수를 작성하려 합니다 . 빈칸을 채워 전체 코드를 완성해주세요
def find(parent, u):
    if u == parent[u]:
        return u
    parent[u] = find(parent, parent[u]) # root 값을 찾을 때까지 현재 node의 부모도 find
    return parent[u]

def merge(parent, u, v):
    u = find(parent, u)
    v = find(parent, v)
    if u == v:
        return True
    # @@@
    parent[u] = v
    return False

def solution(n, connections):
    answer = 0
    # parent = @@@
    parent = [i for i in range(n+1)] # 0,1,2,3,4,5 .... n
    for i, connection in enumerate(connections):
        if merge(parent, connection[0], connection[1]):
            answer = i + 1
            break
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n = 3
connections = [[1, 2], [1, 3], [2, 3]]
ret = solution(n, connections)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")