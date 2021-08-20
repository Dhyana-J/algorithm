# 우선순위 큐를 사용하여 시간복잡도를 훨씬 낮춘다.

import heapq
import sys
import time
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

s = time.time()
def dikstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하고, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        # 최단거리 가장 짧은 노드에 대한 정보 꺼내기
        dist,now = heapq.heappop(q)
        # 현재 노드가 이미 처리된적이 있으면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들 확인
        for i in graph[now]:
            cost = dist+i[1] # 해당 노드까지 거리 + 다른 노드로의 거리 c
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dikstra(start)
for i in range(1,n+1):
    if distance[i]==INF:
        print('INFINITY')
    else:
        print(distance[i])

print('time : ',time.time()-s)        
