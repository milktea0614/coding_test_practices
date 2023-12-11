import sys

"""
My Answer : https://blog.naver.com/milktea0614/222504586184
"""

inf = sys.stdin
T = inf.readline();
for t in range(0, int(T)):
    Answer = 0;
    #############################################################################################
    n_num = int(inf.readline())
    n_list = inf.readline().split()
    for j in range(0,n_num):
        temp = int(n_list[j])
        Answer = Answer ^ temp
        j+=1;
    #############################################################################################
    # Print the answer to standard output(screen).
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()