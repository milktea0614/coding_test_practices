import datetime
import itertools

def make_primenum_list(p_length):
    """
    '에라토스테네스의 채' 이론에 의거하여 소수를 모두 선별
    1. 2부터 소수를 구하고자 하는 구간의 모든 수 나열
    2. 2는 소수 임으로 2의 배수를 모두 지운다
    3. 3은 소수 임으로 3의 배수를 모두 지운다
    4. 5는 소수 임으로 5의 배수를 모두 지운다
    5. 2~4와 같은 과정을 반복한다.

    :param p_length: 만들수 있는 숫자의 최대 자릿 수 (ex.1234의 경우 4)
    :return: index가 숫자이며 value가 1이면 소수 0이면 소수가 아닌 리스트
    """

    max_num = (10 ** p_length)-1
    max_sqrt_of_max_num = int(max_num ** 0.5)

    result = [True] * max_num
    result[0] = False
    result[1] = False

    for i in range(2, max_sqrt_of_max_num+1):
        if result[i]==True:
            for j in range(i*2, max_num, i):
                result[j] = False

    return result

def solution(numbers):
    answer = 0
    # numbers : string, 0~9로 이루어진 숫자, 길이 1~7 최대 숫자 : 9,999,999

    # time1 = datetime.datetime.now()
    prime_list = make_primenum_list(len(numbers))
    # time2 = datetime.datetime.now()
    # print(time2-time1)

    # 순열 리스트 제작
    all_permutations_list = []
    for i in range(0, len(numbers)):
        t_list = list(map(int, map(''.join, itertools.permutations(numbers, i + 1))))
        all_permutations_list.extend(t_list)

    # 순열 리스트에서 중복 제거
    t_set = set(all_permutations_list)
    t_permutaions = list(t_set)

    for j in range(0, len(t_permutaions)):
        if prime_list[t_permutaions[j]] == True:
            answer+=1

    return answer


if __name__ == '__main__':

    input1 = ["17", "011", "9876543"] #3, 2

    for i in range(0, len(input1)):
        answer = solution(input1[i])
        print(answer)