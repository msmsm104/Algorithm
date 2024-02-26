# prefix.py
# 접두사 확인

# 입력값
numbers = ["12","123","1235","567","88"]

# 출력값
answer = True

def solution(numbers):

    hash_map = {}

    # hash_map에 key_value 형식으로 저장
    # 시간 복잡도 O(N)
    for number in numbers:
        hash_map[number] = True

    # print(hash_map.get("1212", False))
    for number in numbers:
        prefix = ""
        for char in number:
            prefix += char
            if hash_map.get(prefix, False) and prefix != number:
            # if prefix in hash_map and prefix != number:
                return False

    return True
            

print(solution(["123","456","789"]))