""" Graph """
# Node(노드)와 Edge(간선)로 구성. Node를 Vertex(정점)라고도 한다
# 두 노드가 간선으로 연결되어있다면, 두 노드는 adjacent(인접)하다
# 프로그래밍으로 그래프는 인접행렬, 인접리스트 두 가지 방식으로 표현할 수 있다.
# Adjacent Matrix(인접행렬) : 2차원 배열로 그래프의 연결관계를 표현하는 방식
# Adjacent List(인접리스트) : 리스트로 그래프의 연결관계를 표현하는 방식

""" 
    인접 행렬은 모든 관계를 저장하므로, 메모리가 불필요하게 낭비된다. 하지만 데이터 접근 속도가 상대적으로 빠르다.
    인접 리스트는 연결된 정보만 저장하므로, 메모리를 효율적으로 사용한다. 하지만 데이터 접근 속도가 상대적으로 느리다.
"""

""" Adjacent Matrix Graph """
# 다른언어의 배열을 파이썬에서는 리스트로 배열 표현가능하므로 리스트 사용
# INF = 999999999
# graph = [
#     [0,7,5],
#     [7,0,INF],
#     [5,INF,0]
# ]

# print(graph)


""" Adjacent List Graph """
# index는 노드번호, 튜플은 (노드,비용)
graph = [[] for _ in range(3)]
graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((1,7))
graph[2].append((0,5))

print(graph)
