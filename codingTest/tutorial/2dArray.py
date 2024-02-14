# 2dArray.py

# 입력값 num_list, n
num_list = [1,2,3,4,5,6,7,8]
n = 2

# for i in range(0, len(num_list), 2):
#     # print(i, i + 2)
#     print(num_list[i:i+2])

def make_2dArray(num_list, n):
    # answer = []
    # for i in range(0, len(num_list), n):
    #     answer.append(num_list[i:i+n])
    answer = [num_list[i: i + n] for i in range(0, len(num_list), n)]
    return answer

print(make_2dArray(num_list, n))