# 실전문제 2 - 도시 분할 계획
# 최소 신장 트리를 찾은 후에, 가장 비용이 큰 간선을 제거하면 최소 신장 트리가 2개의 부분 그래프로 나누어진다.
# 즉, 두 마을이 생긴다.

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드와 간선의 개수 입력받기
v,e = map(int,input().split())
parent = [0]*(v+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

# 간선을 비용순으로 정렬
edges.sort()
last = 0 # 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선

# 간선 하나씩 확인
for edge in edges:
    cost,a,b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        last = cost

print(result-last)

"""
7 12 
1 2 3 
1 3 2 
3 2 1 
2 5 2 
3 4 4 
7 3 6 
5 1 5 
1 6 2 
6 4 1 
6 5 3 
4 5 3 
6 7 4
"""

