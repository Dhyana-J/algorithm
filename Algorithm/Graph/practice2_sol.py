# 실전문제2 - 미로 탈출
# 탈출구까지 최단경로 구하기

from collections import deque

n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input()))) # 공백 없이 입력 들어오므로, 그냥 문자열 순회

# 이동할 네 방향 (상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS 소스코드 구현
def bfs(x,y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))

    #큐 빌 때 까지 반복
    while queue:
        x,y = queue.popleft()
        for i in range(4): # 상하좌우 탐색
            nx = x+dx[i]
            ny = y+dy[i]

            # 미로 벗어난 경우 무시
            if nx < 0 or nx >= n or nx < 0 or ny >= m:
                continue
            # 벽 무시
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

    # 가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))
print('============')

for i in graph:
    for j in i:
        print(j,end=' ')
    print('')
