
# 서로소 집합 (공통 원소가 없는 두 집합)

"""
* 서로소 집합 자료구조
- 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
- union과 find 두 연산으로 조작할 수 있다. 그래서 union-find 자료구조로도 불림
"""


# def find_parent(parent,x):
#     # 루트 노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출
#     if parent[x]!=x:
#         return find_parent(parent,parent[x])
#     return x

def find_parent(parent,x): # 경로 압축 기법 적용
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v,e = map(int,input().split())
parent = [0]*(v+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a,b = map(int,input().split());
    union_parent(parent,a,b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합:',end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ',end='')
for i in range(1,v+1):
    print(parent[i],end=' ')