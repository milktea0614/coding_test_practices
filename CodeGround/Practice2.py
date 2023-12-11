import sys

"""
My Answer : https://blog.naver.com/milktea0614/222504592390
"""

inf = sys.stdin
T = inf.readline();
for t in range(0, int(T)):
    Answer=0;
#############################################################################################
    num_person = int(inf.readline());  # score = n, n-1, n-2, ..., 1
    scores = []
    c_max = -1
    for i in range(0, num_person):
        t_score = int(inf.readline())
        scores.append(t_score)
    scores.sort()
    l_max = -1;
    for j in range(0, num_person): #최저 점수 기준으로 최대값들 구하기
        temp = scores[j]+(num_person-j)
        if l_max < temp:
            l_max = temp
        j += 1;
    for z in range(0, num_person):
        temp_score = scores[z] + num_person
        if l_max <= temp_score:
            Answer += 1;
    #############################################################################################
	# Print the answer to standard output(screen).
    print('Case #%d' %(int(t)+1))
    print(Answer)
inf.close()