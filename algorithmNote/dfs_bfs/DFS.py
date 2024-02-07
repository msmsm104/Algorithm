# DFS.py
# 깊이 우선 탐색 알고리즘 
# 자료구조 - 그래프 -> 노드(node), 간선(edge)로 구성.

# 그래프 표현 방식
# 1. 인접 행렬
# 2. 인접 리스트

INF = 1e9 # 무한의 비용 선언

# 2차원 리스트(인접행렬)를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

# 인접 리스트 방식 - 연결 리스트라는 자료구조를 이용해 구현
# graph_list = [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]
graph_list = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장 (노드, 거리)
graph_list[0].append((1, 7))
graph_list[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장
graph_list[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장
graph_list[2].append((0, 5))

print(graph)
print(graph_list)

