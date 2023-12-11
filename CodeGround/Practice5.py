import sys

"""
My Answer : https://blog.naver.com/milktea0614/222507015602
"""

P = 1000000007 # integer 중 가장 큰 소수
NM2_Max = 2000002 # N+M+2의 최대값

def get_factorial_mod_list():
    """
    1!~(N+M+2)!까지의 결과값을 각각 P로 나눈 나머지를 저장하는 배열 생성 및 반환
    P는 소수여야 함.
    ex. list[0]=1, list[1]=(list[0]*1)%P, list[2]=(list[1]*2)%P, list[3]=(list[2]*6)%P, ..., list[n+m+2]=(list[n+m+1]*(n+m+2))%P
    :return: list = factorial mod list
    """
    list=[1]

    for i in range(1,NM2_Max+1):
        list.append((list[-1]*i)%P) # factorial(n) mod P

    return list

def get_mod_pow(x,power):
    """
    x^power % P로 나눈 나머지를 구하는 함수
    :param x: 제곱이 되어지는 숫자
    :param power: 제곱할 횟수
    :return: x^(power) % P
    """
    rem = 1 # remainder

    while power > 0:
        if power%2 !=0:
            rem = (rem*x)%P # ((rem%P)*(x%P))%P
        x = ((x*x)%P) # x^2 % P
        if power%2 ==0:
            power = int(power/2)
        else:
            power = int(power-1)/2

    return rem

if __name__ == '__main__':
    inf = sys.stdin
    T = inf.readline();
    fl = get_factorial_mod_list()

    for t in range(0, int(T)):
        Answer = 0;

        #############################################################################################
        # 주요 알고리즘 : 파스칼의 삼각형, 이항계수, 모듈러 연산(+파르마의 소정리), 파르마의 소정리 응용:제곱수
        # A = (n+m+2)!, B = (m+1)!(n+1)!
        # Answer = (((A%P)*(B^(P-2)%P))%P-1)%P

        temp = inf.readline().split()
        n = int(temp[0])
        m = int(temp[1])

        # B^(P-2)%P = ((m+1)!(n+1!))^(P-2)%P
        mod2 = get_mod_pow((fl[m + 1] * fl[n + 1]) % P, P - 2)

        # A%P = (n+m+2)!%P = factorial_storage[n+m+2]
        mod1 = fl[n+m+2]

        Answer = (mod1 * mod2 - 1) % P

        #############################################################################################

        # Print the answer to standard output(screen).
        print('Case #%d' % (int(t) + 1))
        print(Answer)
    inf.close()