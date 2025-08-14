import sys
from collections import deque

input = sys.stdin.readline
n, m= map(int,input().split())
indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]
for _ in range(m):
    # 방향 그래프의 모든 간선 정보를 입력 받기
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능(a가 b 보다 크다)
    # 진입 차수를 1 증가
    indegree[b] += 1

# 진입 차수가 0인 모든 노드를 큐에 넣는다
queue = deque()
for i in range(len(indegree)):
    if indegree[i] == 0:
        queue.append(i)

result = [] # 알고리즘 수행 결과를 담을 리스트
# 큐가 빌 때까지 다음의 과정을 반복한다.
while queue:
    # 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
    # (해당 원소와 연결된 노드들의 진입차수에서 1 빼기)
    node = queue.popleft()
    result.append(node)
    for i in graph[node]:
        indegree[i] -= 1
        # 새롭게 진입차수가 0이되는 노드를 큐에 삽입
        if indegree[i] == 0:
            queue.append(i)
result.pop(0) # 0 번째 인덱스 지우기
for i in result:
    print(i,end = " ")