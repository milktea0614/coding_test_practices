def solution(arr1, arr2):
    # C[i][j] = A[i][1]B[1][j] + A[i][2]B[2][j] + ... + A[i][n]*B[n][j]

    num_x = len(arr1)
    num_n = len(arr1[0])
    num_y = len(arr2[0])

    answer = [[0 for i in range(0, num_y)] for j in range(0, num_x)]

    for j in range(0, num_y):
        for i in range(0, num_x):
            for t in range(0, num_n):
                answer[i][j] += arr1[i][t]*arr2[t][j]

    return answer


if __name__ == '__main__':
    input1 = [[[1, 4], [3, 2], [4, 1]], [[2, 3, 2], [4, 2, 4], [3, 1, 4]]]
    input2 = [[[3, 3], [3, 3]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]]
    expected = [[[15, 15], [15, 15], [15, 15]], [[22, 22, 11], [36, 28, 18], [29, 20, 14]]]


    for i in range(len(input1)):
        actual = solution(input1[i], input2[i])
        if actual == expected[i]:
            print("[통과]\n\tActual="+str(actual)+"\n\tExpected="+str(expected[i]))
        else:
            print("[실패]\n\tActual="+str(actual)+"\n\tExpected="+str(expected[i]))