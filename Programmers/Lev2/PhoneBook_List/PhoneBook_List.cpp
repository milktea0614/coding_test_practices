#include <string>
#include <vector>
#include <algorithm>

#include<iostream>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;

    sort(phone_book.begin(), phone_book.end());

    for (int i = 0; i < phone_book.size() - 1; i++) {
        string str_current = phone_book[i];
        string str_next = phone_book[i + 1].substr(0, str_current.length());

        if (str_next == str_current) {
            answer = false;
            break;
        }
    }


    return answer;
}

int main() {

    vector<string> t_input = {"119", "97674223", "1195524421"}; // false
    cout << solution(t_input) << endl;

}