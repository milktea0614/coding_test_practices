import sys
import math

"""
My Answer : https://blog.naver.com/milktea0614/222505241388
"""


inf = sys.stdin

T = inf.readline();

for t in range(0, int(T)):
    Answer = 0;

    #############################################################################################

    # 추가 점수 계산 0~A : Bull(50), B~C : Trifle(*3), D~E : Double(*2), E~: 0, 나머지 Single (A~B, C~D)
    # N = 다트 개수
    # - 30000 <= x,y <= 30000
    # 중심 : 0,0
    # output = score

    temp = inf.readline().split()
    area_list=[]
    for i in range(0, len(temp)): # Covert to Integer
        area_list.append(int(temp[i]))

    dart = int(inf.readline())

    # 20칸, 1칸당 18도
    scores_p = [6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11] # 9도*[(6)0~1, (13)1~3, (4)3~5, (18)5~7, (1)7~9, (20)9~11, (5)11~13, (12)13~15, (9)15~17, (14)17~19, (11)19~20
    scores_m = [6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11] # -9도*[(6)0~1, (10)1~3, (15)3~5, (2)5~7, (17)7~9, (3)9~11, (19)11~13, (7)13~15, (16)15~17, (8)17~19, (11)19~20

    for i in range(0,dart):
        dart_location = inf.readline().split()
        x = float(dart_location[0])
        y = float(dart_location[1])

        # 점수 범위 - r 구하기
        r = ((x*x)+(y*y)) ** 0.5

        # 점수 찾기 - 각도 얻기
        angle = (math.atan2(y,x)) * 180 / math.pi # radian = atan(y/x), angle = radian * 180 / Math.pi
        # 점수 찾기 - 점수 얻기
        temp_score = 0
        temp = angle / 9
        if angle >= 0:
            if temp <= 1:
                temp_score = scores_p[0]
            elif temp <=3:
                temp_score = scores_p[1]
            elif temp <=5:
                temp_score = scores_p[2]
            elif temp <= 7:
                temp_score = scores_p[3]
            elif temp <= 9:
                temp_score = scores_p[4]
            elif temp <= 11:
                temp_score = scores_p[5]
            elif temp <= 13:
                temp_score = scores_p[6]
            elif temp <= 15:
                temp_score = scores_p[7]
            elif temp <= 17:
                temp_score = scores_p[8]
            elif temp <= 19:
                temp_score = scores_p[9]
            else:
                temp_score = scores_p[10]
        else:
            temp = abs(temp)
            if temp <= 1:
                temp_score = scores_m[0]
            elif temp <= 3:
                temp_score = scores_m[1]
            elif temp <= 5:
                temp_score = scores_m[2]
            elif temp <= 7:
                temp_score = scores_m[3]
            elif temp <= 9:
                temp_score = scores_m[4]
            elif temp <= 11:
                temp_score = scores_m[5]
            elif temp <= 13:
                temp_score = scores_m[6]
            elif temp <= 15:
                temp_score = scores_m[7]
            elif temp <= 17:
                temp_score = scores_m[8]
            elif temp <= 19:
                temp_score = scores_m[9]
            else:
                temp_score = scores_m[10]

        # 추가 점수 계산 0~A : Bull(50), B~C : Trifle(*3), D~E : Double(*2), E~: 0, 나머지 Single (A~B, C~D)
        if r <= area_list[0]: # 0~A : Bull(50)
            Answer+=50
        elif r >= area_list[1] and r <= area_list[2] : # B~C : Trifle(*3)
            Answer += (temp_score*3)
        elif r >= area_list[3] and r <= area_list[4] : # D~E : Double(*2)
            Answer += (temp_score * 2)
        elif r > area_list[4] : # E~: 0
            Answer +=0
        else:
            Answer += temp_score

    #############################################################################################

    # Print the answer to standard output(screen).
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()