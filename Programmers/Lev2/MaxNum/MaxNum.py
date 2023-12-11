def solution(numbers):
    answer = ''

    #string 변환
    string_numbers = []
    for i in range(0, len(numbers)):
        string_numbers.append(str(numbers[i]))

    string_numbers.sort(key=lambda x:x*4, reverse=True)
    answer = str(int(''.join(string_numbers)))
    return answer

if __name__ == '__main__':
    t_input = [ [6, 10, 2], [3, 30, 34, 5, 9], [3, 30, 33,330]] # "6210", "9543330", "33333030"

    for i in range(0, len(t_input)):
        print(solution(t_input[i]))
