# 전보

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 도시 개수 n, 통로 개수 m, 메세지 보내는 도시 c
n,m,c = map(int,input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    # 특정 도시 x에서 다른 도시 y로 메세지 전달되는 시간 z
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dikstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for info in graph[now]:
            cost = dist+info[1]
            if cost < distance[info[0]]:
                distance[info[0]] = cost
                heapq.heappush(q,(cost,info[0]))

dikstra(c)

max_distance = 0
count = 0

for i in distance:
    if i!=INF:
        max_distance=max(max_distance,i) # 메세지 보내는데 가장 오래걸린 시간 저장
        count+=1

print(count-1,max_distance)