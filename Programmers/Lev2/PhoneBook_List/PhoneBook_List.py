def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(0, len(phone_book) - 1):
        temp_sub_string = phone_book[i + 1][0:len(phone_book[i])]
        if temp_sub_string == phone_book[i]:
            answer = False
            break

    return answer

if __name__ == '__main__':

    input1 = ["119", "97674223", "1195524421"]

    answer = solution(input1)

    print(answer)

