# 신장 트리 (Spanning Tree) - 하나의 그래프가 있을 때, 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# Minimum Spanning Tree - 비용 합이 최소가 되는 신장 트리
"""
* Kruscal Algorithm

- 최소 신장 트리를 찾을 수 있는 대표적인 알고리즘이다. 
- 가장 적은 비용으로 모든 노드를 연결할 수 있다.
- 그리디 알고리즘으로 분류된다.

"""

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력받기
v,e = map(int,input().split())
parent = [0] * (v+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

# 모든 간선 정보 입력받기
for _ in range(e):
    a,b,cost = map(int,input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost,a,b))

# 간선 비용순 정렬
edges.sort()

# 간선 하나씩 확인
for edge in edges:
    cost,a,b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
    
print(result)


"""
7 9
1 2 29
1 5 75
2 3 35
2 6 34 
3 4 7
4 6 23
4 7 13 
5 6 53 
6 7 25
"""