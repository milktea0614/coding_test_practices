# Level 3

class music:
    def __init__(self):
        self.sum = 0
        self.songs = []

    def add_plays(self, p_index, p_plays):
        self.songs.append((p_index, p_plays))

    def add_sum(self, p_num):
        self.sum = self.sum+p_num

    def get_sum(self):
        return self.sum

    def get_plays(self):
        return self.songs


def solution(genres, plays):
    answer = []

    # key : 장르, value : sum, dict
    temp_hash = {}

    for i in range(0, len(genres)):
        if genres[i] in temp_hash:
            current_value = (temp_hash[genres[i]])
            current_value.add_sum(plays[i])
            current_value.add_plays(i,plays[i])
            temp_hash[genres[i]] = current_value

        else:
            t = music()
            t.add_sum(plays[i])
            t.add_plays(i,plays[i])
            temp_hash[genres[i]] = t


    sorted_hash = sorted(temp_hash.items(), key = lambda itmes : itmes[1].sum, reverse=True)

    for k in sorted_hash:
        t_plays = temp_hash[k[0]].get_plays()

        # 정렬 우선순위! x[1]을 우선
        t_plays.sort(key = lambda x:(-x[1],x[0]))

        if len(t_plays) < 2:
            t_range = len(t_plays)
        else:
            t_range = 2

        for i in range(0, t_range):
            answer.append(t_plays[i][0])

    return answer


if __name__ == '__main__':

    input1 = ["classic", "pop", "kpop", "classic"]
    input2 = [300, 400, 500, 300]

    answer = solution(input1,input2)

    print(answer)

    input1 = ["classic", "pop", "classic", "classic", "pop"]
    input2 = [500, 600, 150, 800, 2500]

    answer = solution(input1, input2)

    print(answer)