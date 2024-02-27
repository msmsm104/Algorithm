# clothes.py
# 의상 문제

# 입력값
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

# 출력값
result = 0

# 해시맵 (딕셔너리)
hash_map = {}
for x in map(lambda x: x[1], clothes):
    hash_map[x] = []

for x in clothes:
    hash_map[x[1]].append(x[0])

print(hash_map)

for key, value in hash_map.items():
    if len(value) > 1:
        for stuff in value:
            print(stuff)
    else:
        print(value[0])



