def solution(prices):
    answer = []

    # answer 0으로 초기화
    answer = [0 for i in range(len(prices))]

    my_stack = []

    for current_index in range(0, len(prices)):
        if len(my_stack) < 1:
            my_stack.append([prices[current_index], current_index])
        else:
            t_element = my_stack[-1]

            while (len(my_stack) > 0) and (t_element[0] > prices[current_index]):
                answer[t_element[1]] = current_index - t_element[1]
                my_stack.pop()
                if len(my_stack)>0:
                    t_element = my_stack[-1]

            my_stack.append([prices[current_index], current_index])


    while len(my_stack) > 0:
        t_ele = my_stack.pop()
        t_index = t_ele[1]
        answer[t_index] = current_index - t_index

    return answer

if __name__ == '__main__':
    input = [[1,2,3,2,3], [3,3,3,3,3,3], [5,5,3,3,4,3,1], [5,2,6,3]]
    expect_result = [[4,3,1,1,0], [5,4,3,2,1,0], [2,1,4,3,1,1,0], [1, 2, 1, 0]]

    for i in range(0, len(input)):
        print(solution(input[i]), expect_result[i])
