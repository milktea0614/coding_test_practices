def solution(citations):
    answer = 0

    citations.sort()

    length = len(citations)

    for i in range(0, length):
        h_index = length-i

        if citations[i] >= h_index:
            answer = h_index;
            break

    return answer

if __name__ == '__main__':

    input1 = [[3, 0, 6, 1, 5], [2, 0, 7, 7, 10]] #3

    for i in range(0, len(input1)):
        answer = solution(input1)

    print(answer)

