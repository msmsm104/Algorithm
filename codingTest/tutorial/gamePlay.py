# gamePlay.py

# 입력값
# keyinput = ["left", "right", "up", "right", "right"]
# board = [11, 11]


def gamePlay(keyInput, board):
    # 출력값
    result = []

    # 시뮬레이션 알고리즘
    keyToIndex = {
        "left" : 0,
        "right" : 1,
        "down" : 2,
        "up": 3
    }

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    x = 0
    y = 0

    for i in range(len(keyInput)):
        idx = keyToIndex[keyInput[i]]
        nx = x + dx[idx]
        ny = y + dy[idx]
        if nx >= -(board[0]//2) and nx <= (board[0]//2) and ny >= -(board[1]//2) and ny <= (board[1]//2):
        # if nx <= board[0] and ny <= board[1]:
            x, y = nx, ny
        
    return [x, y]

print(gamePlay(["down", "down", "down", "down", "down"], [7, 9]))