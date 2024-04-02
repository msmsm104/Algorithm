# que.py
# 스택, 큐 문제

from collections import deque


def solution(priorities, location):
    idx_array = [0] * len(priorities)
    idx_array[location] += 1
    idx_que = deque(idx_array)

    # 출력값
    result = 0

    # 입력값 properties와 동일한 길이의 인덱스를 갖는 배열 
    # properties 값을 기준으로 로직을 실행
    que = deque(priorities)
    result_array = []
    result_idx_array = []

    # 큐에서 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있는지 비교 (que의 길이가 0이 될때까지)
    while len(que) > 0:
        # 실행 대기 큐에서 대기중인 프로세스 하나를 꺼냅니다.
        max_process = max(que)
        process = que.popleft()
        idx_process = idx_que.popleft()

        if max_process == process:
            result_array.append(process)
            result_idx_array.append(idx_process)

        else:
            que.append(process)
            idx_que.append(idx_process)

    result += result_idx_array.index(1) + 1

    return result

print(solution([2,1,3,2], 2))




