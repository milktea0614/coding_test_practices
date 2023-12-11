def shift_left_string(p_s):
    if len(p_s) > 1:
        result = p_s[1:] + p_s[0]
    else:
        result = p_s
    return result


def check_correct_string(p_s):
    # [[](){}{([])}] - [], (), {} 제거 - [{}{()}] - [{}]
    # [[[[{([{}])}]]]] - [[[[{([])}]]]] - [[[[{()}]]]]
    for i in range(0, int(len(p_s) / 2) + 1):  # 줄어든다면 최소 2개씩 줄어들기 때문에
        temp1 = p_s.replace("()", "")
        temp2 = temp1.replace("[]", "")
        temp3 = temp2.replace("{}", "")
        p_s = temp3

    if len(p_s) > 0:
        return 0
    else:
        return 1


def solution(s):
    answer = 0

    if len(s) % 2 > 0:  # 문자열의 길이가 홀수면 올바른 괄호가 아님
        answer = 0
    else:
        for i in range(0, len(s)):
            answer += check_correct_string(s)
            s = shift_left_string(s)

    return answer

if __name__ == '__main__':
    t_input = [ "[](){}", "}]()[{", "[)(]", "}}}"] # 3, 2, 0, 0
    for i in range(0, len(t_input)):
        print(solution(t_input[i]))
