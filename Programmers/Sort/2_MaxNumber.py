
def solution(numbers):
    answer = ''

    #string 화
    string_numbers = []
    for i in range(0, len(numbers)):
        string_numbers.append(str(numbers[i]))

    # 앞자리가 가장 큰수를 기준으로 정렬
    string_numbers.sort(key=lambda x: x*3)
    string_numbers.reverse()

    answer = str(int(''.join(string_numbers)))
    return answer

if __name__ == '__main__':

    input1 = [3, 30, 34, 5, 9]

    answer = solution(input1)

    print(answer)

    input1 = [6, 10, 2]

    answer = solution(input1)

    print(answer)