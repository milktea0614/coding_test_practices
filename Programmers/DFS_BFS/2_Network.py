# Lev3

def solution(n, computers):
    answer = 0

    # 노드 : 컴퓨터 , 연결 : 네트워크 -> 네트워크 갯수 세기
    t_list = []
    for i in range(0, n):
        for j in range(0, n):
            if (i != j) and (computers[i][j] == 1):
                if i<=j:
                    t_list.append([i, j])
                else:
                    t_list.append([j, i])

    t_items = list(set([tuple(set(item)) for item in t_list]))
    print(t_items)

    answer = len(t_items)
    return answer


if __name__ == '__main__':

    input = [[3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]], [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]]] # 2 / 1

    for i in range(0, len(input)):
        answer = solution(input[i][0],input[i][1])
        print(answer)