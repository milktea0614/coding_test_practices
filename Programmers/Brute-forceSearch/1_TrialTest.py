# Lev2

def solution(answers):
    answer = []  # 정답

    # 1번 수포자 :  1, 2, 3, 4, 5, 반복 (5개)
    person1 = [1, 2, 3, 4, 5]
    # 2번 수포자 : 2, 1, 2, 3, 2, 4, 2, 5, 반복 (8개)
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    # 3번 수포자 : 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 반복 (10개)
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = [0, 0, 0]

    for i in range(0, len(answers)):
        t_answer = answers[i]

        if t_answer == person1[i % 5]:
            count[0] += 1
        if t_answer == person2[i % 8]:
            count[1] += 1
        if t_answer == person3[i % 10]:
            count[2] += 1

    max_count = max(count)

    for j in range(0, len(count)):
        if max_count == count[j]:
            answer.append(j + 1)

    return answer

if __name__ == '__main__':

    input1 = [[1,2,3,4,5], [1,3,2,4,2]] #[1], [1,2,3]

    for i in range(0, len(input1)):
        answer = solution(input1[i])
        print(answer)