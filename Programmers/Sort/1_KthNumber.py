# Level 1

def solution(array, commands):
    answer = []

    for i in range(0, len(commands)):
        t_command = commands[i]
        temp_array = array[t_command[0] - 1:t_command[1]]
        temp_array.sort()
        answer.append(temp_array[t_command[2] - 1])

    return answer


if __name__ == '__main__':

    input1 = [1, 5, 2, 6, 3, 7, 4]
    input2 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    answer = solution(input1,input2)

    print(answer)
