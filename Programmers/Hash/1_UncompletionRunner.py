# Level 1

def solution(participant, completion):
    answer = ''

    temp_dict = {}

    for i in range(0,len(participant)):

        temp_key = participant[i]

        if temp_key in temp_dict:
            current_value = temp_dict[participant[i]]
            temp_dict[temp_key] = current_value+1
        else:
            temp_dict[temp_key] = 1

    for i in range(0, len(completion)):
        temp_key = completion[i]
        current_value = temp_dict[temp_key]
        temp_dict[temp_key] = current_value-1

    for key in temp_dict.keys():
        if temp_dict[key] > 0:
            answer = key
            break

    return answer

if __name__ == '__main__':

    input1 = ["mislav", "stanko", "mislav", "ana"]
    input2 = ["stanko", "ana", "mislav"]

    answer = solution(input1, input2)

    print(answer)

