def solution(priorities, location):
    answer = 0

    t_my_list = []

    for i in range(0, len(priorities)):
        t_my_set = [i, priorities[i]]  # index, value 쌍
        t_my_list.append(t_my_set)

    current = 0

    while len(t_my_list) != 0:
        t_set = t_my_list.pop(0)
        t_flag = False

        for temp in t_my_list:
            if temp[1] > t_set[1]:
                t_flag = True

        if t_flag:
            t_my_list.append(t_set)
        else:
            current+=1
            if t_set[0] == location:
                answer = current
                break

    return answer

if __name__ == '__main__':

    input = [[[2, 1, 3, 2], 2], [[1, 1, 9, 1, 1, 1], 0]] # 2 / 1

    for i in range(0, len(input)):
        answer = solution(input[i][0],input[i][1])
        print(answer)