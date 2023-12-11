import sys

"""
My Answer : https://blog.naver.com/milktea0614/222504603343
"""

inf = sys.stdin
T = inf.readline();
for t in range(0, int(T)):
    Answer = 0;
    #############################################################################################
    temp = inf.readline().split()
    N = int(temp[0])
    K = int(temp[1])
    temp_list = inf.readline().split()
    lists = []
    for i in range(0, len(temp_list)): #왜 굳이굳이 바꿔줘야 하는 과정이 필요하지?
        lists.append(int(temp_list[i]))
    lists.sort(reverse=True)
    for i in range(0, K):
        Answer += int(lists[i])
    #############################################################################################
    # Print the answer to standard output(screen).
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()