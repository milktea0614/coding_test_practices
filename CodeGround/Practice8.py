import sys

"""
My Answer : https://blog.naver.com/milktea0614/222586104750
"""
inf = sys.stdin

T = inf.readline();

for t in range(0, int(T)):
    Answer = 0;

    #############################################################################################

    # init
    N = int(inf.readline())
    input_list = inf.readline().split()
    height_list = [0]  # 맨 처음 블록 높이 앞에는 0 높이의 블록 추가 (양 옆에 추가한다고 해서 값에 영향을 주지 않음)

    for i in range(0, N):
        height_list.append(int(input_list[i]))
    height_list.append(0)  # 맨 끝 블록 높이 뒤에 0 높이의 블록 추가 (양 옆에 추가한다고 해서 값에 영향을 주지 않음)

    # -> 방향으로 삭제 횟수 판단 (1차)
    block_remove = [0]
    for i in range(1, len(height_list)):  # -> 방향
        left = block_remove[i - 1] + 1
        current = height_list[i]
        block_remove.append(min(left, current))

    # <- 방향으로 삭제 횟수 판단 (2차) (양반향 이기 때문에)
    for i in range(len(height_list) - 2, 1, -1):
        right = block_remove[i + 1] + 1
        current = block_remove[i]  # min(block_remove[i-1]+1, height_list[i])
        block_remove[i] = min(current, right)

    # block_remove에서 max 값 찾기
    Answer = max(block_remove)

    #############################################################################################
    # Print the answer to standard output(screen).
    print('Case #%d' % (int(t) + 1))
    print(Answer)

inf.close()