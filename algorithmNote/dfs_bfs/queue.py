# queue.py
# 큐 자료구조를 구현하기 위해 collections 라이브러리 사용

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()

print(queue)