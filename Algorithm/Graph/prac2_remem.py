# 미로 길찾기

from collections import deque

n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=n or nx<0 or ny>=m or ny<0:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                if nx==0 and ny==0: # 시작지점 못돌아오게 막기
                    continue
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]





print(bfs(0,0))

for i in graph:
    for j in i:
        print(j,end=' ')
    print()