class user_info:
    def __init__(self):
        self.report_id = [] # 신고한 ID
        self.reported_count = 0 # 신고 당한 횟수

    def increase_reported_count(self):
        self.reported_count+=1

    def add_report_id(self, p_id):
        self.report_id.append(p_id)

    def get_report_id(self):
        return self.report_id

    def get_reported_count(self):
        return self.reported_count


def solution(id_list, report, k):
    answer = []
    t_user = {}
    t_stop = []

    # report 중복 제거 (같은 유저의 같은 유저 신고 중복 count X)
    report_set = set(report)
    report_list = list(report_set)

    # t_user 해시 dict, 정지 아이디 세기
    for i in range(0, len(report_list)):
        reporter = report_list[i].split()[0]
        reported = report_list[i].split()[1]

        # 신고한 사람
        if reporter in t_user:
            temp = t_user[reporter]
            temp.add_report_id(reported)
            t_user[reporter] = temp
        else:
            temp = user_info()
            temp.add_report_id(reported)
            t_user[reporter] = temp

        # 신고된 사람
        if reported in t_user:
            temp = t_user[reported]
            temp.increase_reported_count()
            t_user[reported] = temp
        else:
            temp = user_info()
            temp.increase_reported_count()
            t_user[reported] = temp

        if temp.get_reported_count() >= k:
            t_stop.append(reported)

    t_stop_set = set(t_stop)

    for t_id in id_list:
        count = 0
        if t_id in t_user:
            t_set = set(t_user[t_id].get_report_id())
            count = len(t_set & t_stop_set)

        answer.append(count)

    return answer


if __name__ == '__main__':

    input1 = ["muzi", "frodo", "apeach", "neo"]
    input2 = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    input3 = 2

    answer = solution(input1,input2, input3) #[2,1,1,0]

    print(answer)

    input1 = ["con", "ryan"]
    input2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
    input3 = 3

    answer = solution(input1,input2, input3) # [0, 0]

    print(answer)