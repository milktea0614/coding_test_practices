# Lev 2

def recursive(p_num, p_result, p_target):
    if len(p_num) == 0:
        if p_target == p_result:
            return 1
        else:
            return 0
    else:
        t_value = p_num[0]
        p_value = p_result+t_value
        m_value = p_result-t_value
        return (recursive(p_num[1:], p_value, p_target) + recursive(p_num[1:], m_value, p_target))


def solution(numbers, target):
    answer = 0
    answer = recursive(numbers, 0, target)

    return answer


if __name__ == '__main__':

    input1 = [[[1, 1, 1, 1, 1],3], [[4, 1, 2, 1],4]] # 5 / 2

    for i in range(0, len(input1)):
        answer = solution(input1[i][0],input1[i][1])
        print(answer)