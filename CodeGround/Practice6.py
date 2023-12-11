import sys

"""
My Answer : https://blog.naver.com/milktea0614/222508181173
"""

inf = sys.stdin

T = inf.readline();

for t in range(0, int(T)):
    Answer = 0;

    #############################################################################################
    # N = 배열의 가로,세로 크기 / K = 움직인 횟수
    # U = 위쪽 / D = 아래쪽 / L = 왼쪽 / R = 오른쪽
    # Output = 이동 중 방문한 곳의 숫자에 대한 모든 합 (중복 방문 시 중복 합)

    temp = inf.readline().split()
    N = int(temp[0])
    K = int(temp[1])

    # list C 만들기
    list_C = [1]
    for i in range(2,N+1):
        list_C.append(list_C[-1]+i)

    # 이동 문자열 받기
    move = inf.readline()

    # 초기 시작 위치
    x=0
    y=0
    # 초기 시작 위치값 더하기
    Answer += 1 # (0,0) = 1


    # 이동하기
    for j in range(0, K):
        if move[j]=='D': # 아래로 이동
            x +=1
        elif move[j]=='R': #오른쪽으로 이동
            y +=1
        elif move[j]=='U' :# 위로 이동
            x -=1
        else: # 왼쪽으로 이동
            y -=1

        if x+y == 0: #(1)
            t_value = 1
        elif x+y < N:
            if (x+y)%2 == 1: # (2)-① 홀수일때
                t_value = (list_C[(x+y-1)]+(x+1))
            else: # (2)-② 짝수일때
                t_value = (list_C[(x + y)] - x)
        else: # x+y >= N
            # (x,y) + (n-1-x, n-1-y) = n^2+1
            tx = N-1-x
            ty = N-1-y
            if tx+ty == 0:
                t_value = ((N ** 2) + 1) - 1
            elif (tx+ty)%2 ==1:
                t_value = ((N ** 2) + 1) - (list_C[tx+ty-1]+(tx+1))
            else:
                t_value = ((N ** 2) + 1) - (list_C[tx + ty] - tx)

        Answer += t_value

    #############################################################################################

    # Print the answer to standard output(screen).
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()