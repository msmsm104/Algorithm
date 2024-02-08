# maze.py
# 미로탈출

# 입력값
n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if graph[x][y] == 1:
        # 현재 노드 방문처리
        graph[x][y] = 0
        # 재귀 호출
        dfs(x + 1, y)
        dfs(x, y + 1)
    
    if x == n and y == m:
        return True

    
print(dfs(0, 0))

print(graph)


