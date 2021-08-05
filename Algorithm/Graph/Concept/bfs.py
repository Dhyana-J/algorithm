""" Breadth First Search """
# Queue를 사용한다.
# 보통 탐색 시간이 DFS보다 짧게걸린다

from collections import deque

n,m = map(int,input().split())
graph = []

for i in range(n):
    graph.append(list(map(int,input())))

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    # 큐가 빌 때 까지 반복
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

bfs(graph,1,visited)