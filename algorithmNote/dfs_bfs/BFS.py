# BFS.py
# 너비 우선 탐색 알고리즘
# 큐 자료구조를 이용

from collections import deque

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

# 자료구조
q = deque()

node = 1

q.append(node)
visited[node] = True

def bfs(graph, start, visited):
    queue = deque()

    queue.append(start)
    visited[start] = True

    while queue:
        n = queue.popleft()
        print(n, end = " ")
        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(graph, 1, visited)