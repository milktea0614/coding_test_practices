def get_common_divsor(num1, num2):
    result = 1
    t_min = num1
    t_max = num2

    if num1 > num2:
        t_min = num2
        t_max = num1

    for i in range(1, int(t_min ** 0.5) + 1):
        t_div = t_min // i
        if t_min % i == 0 and t_max % i == 0:
            if result < i:
                result = i
        if t_min % t_div == 0 and t_max % t_div == 0:
            if result < t_div:
                result = t_div
                break
    return result


def solution(arr):
    answer = 0

    while len(arr) > 1:
        num1 = arr.pop()
        num2 = arr.pop()
        max_divisor = get_common_divsor(num1, num2)
        t_num1 = num1 // max_divisor
        t_num2 = num2 // max_divisor
        answer = t_num1 * t_num2 * max_divisor
        arr.append(answer)

    answer = arr.pop()
    return answer

if __name__ == '__main__':
    t_input = [[2,6,8,14], [1,2,3]] # 168, 6
    for i in range(0, len(t_input)):
        print(solution(t_input[i]))
