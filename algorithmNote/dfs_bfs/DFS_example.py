# DFS_example.py

# 재귀적으로 구현

def dfs_recursive(graph, v, visited):
    # 현재 위치를 방문 처리
    visited[v] = True
    print(v, end = " ")
    # 방문하지 않은 인접노드
    for node in graph[v]:
        if not visited[node]:
            dfs_recursive(graph, node, visited)



# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표형(1차원 리스트)
visited = [False] * len(graph)

dfs_recursive(graph, 1, visited)

