def solution(brown, yellow):
    answer = []

    t_brown = []  # [[가1,세1], [가2,세2], ..]
    if yellow == 1:  # ㅁ만 됨
        t_brown = [[3, 3]]
    else:
        t_pivot = 1
        for i in range(1, yellow):
            if yellow % i == 0:  # 약수이면
                t_pivot = int(yellow / i)
                if (t_pivot + 2) > (i+2):
                    t_brown.append([t_pivot + 2, i + 2])
                else:
                    t_brown.append([i + 2, t_pivot + 2])
            if i >= t_pivot:
                break

    for i in range(0, len(t_brown)):
        if t_brown[i][0] * t_brown[i][1] == brown + yellow:
            answer = [t_brown[i][0], t_brown[i][1]]

    return answer


if __name__ == '__main__':

    input1 = [[10,2], [8,1], [24,24]] # 4,3 / 3,3 / 8,6

    for i in range(0, len(input1)):
        answer = solution(input1[i][0],input1[i][1])
        print(answer)