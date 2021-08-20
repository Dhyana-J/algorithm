# 미래 도시
INF = (1e9) # 무한 의미하는 값으로 10억 설정

# 노드 개수 및 간선 개수 입력받기
n,m = map(int,input().split())

# 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range (n+1)]

# 자체 간선 (self loop) 비용은 0으로 초기화
for a in range(n+1):
    for b in range(n+1):
        if a==b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용 1이라고 설정
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 최종 목적지 노드 x와 거쳐갈 노드 k를 입력받기
x,k = map(int,input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

# 도달 불가하면 -1
if distance>=INF:
    print('-1')
else:
    print(distance)

"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""