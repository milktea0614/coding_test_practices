# Lev 2

def calculate_day(p_pro, p_speed):
    t_num = (100 - p_pro) % p_speed

    if t_num > 0:
        return int((100 - p_pro) / p_speed) + 1
    else:
        return int((100 - p_pro) / p_speed)


def solution(progresses, speeds):
    answer = []
    t_queue = [] # 앞의 프로세스가 끝나지 않으면 더 나중 프로세스도 안 끝남

    for i in range(0, len(progresses)):
        t_day = calculate_day(progresses[i], speeds[i])

        if (len(t_queue) != 0 and t_queue[-1] < t_day):
            answer.append(len(t_queue))
            t_queue = []

        t_queue.insert(0, t_day)

    answer.append(len(t_queue))

    return answer

