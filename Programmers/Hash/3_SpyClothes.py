# Level 2

def solution(clothes):
    answer = 0

    # key : 의상 종류, value : 의상 갯수(같은 이름을 가진 의상 존재 X)
    temp_hash = {}

    for i in range(0, len(clothes)):
        if clothes[i][1] in temp_hash:
            current_value = temp_hash[clothes[i][1]]
            temp_hash[clothes[i][1]] = current_value + 1
        else:
            temp_hash[clothes[i][1]] = 1

    # {1*(n1+1)(n2+1)...(n?+1)}-1
    # 선택하지 않는 경우의 수가 있어 1 추가, 모든 옷이 선택되지 않은 경우의 수가 있어 -1

    result = 1

    for key in temp_hash.keys():
        result = result * (temp_hash[key] + 1)

    answer = result - 1
    return answer


if __name__ == '__main__':

    input1 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

    answer = solution(input1)

    print(answer)
