import sys

"""
My Answer : https://blog.naver.com/milktea0614/222585419311
"""

if __name__ == '__main__':
    inf = sys.stdin
    T = inf.readline()

    for t in range(0, int(T)):
        Answer = 0
        #############################################################################################
        # list_right init
        list_right = [0]*400001 # 크기가 400,000 인 배열 생성 (인덱스 = sum, 원소값 = 1 or 0)

        # init
        N = inf.readline()
        temp = inf.readline().split()
        input_arr = []

        for N in range(0, int(N)):
            input_arr.append(int(temp[N]))

        # 첫번쨰 원소는 좋은 수가 될 수 없음 (2번째 원소부터 시작)
        for num in range(1, N):

            for x in range(0, num):
                list_right[input_arr[x] + input_arr[num - 1] + 200000] = 1 # 합이 마이너스 일 수 도 있기 때문에

            for x in range(0, num):
                if list_right[input_arr[num] - input_arr[x] + 200000] == 1:
                    Answer += 1
                    break

        #############################################################################################

        # Print the answer to standard output(screen).
        print('Case #%d' % (int(t) + 1))
        print(Answer)
    inf.close()