# 모든 지점에서 다른 모든 지점까지의 최단경로를 모두 구해야 하는 경우 사용함
# 시간 복잡도 O(N^3)

INF = int(1e9) # 무한을 의미하는 값 설정

# 노드 개수와 간선 개수 입력받기
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만드로, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

# 수행된 결과를 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        # 도달할 수 없는 경우, 무한(INFINITY)출력 
        if graph[a][b] == INF:
            print('INFINITY',end=" ")
        else:
            print(graph[a][b],end=" ")
    print()


"""
input
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""