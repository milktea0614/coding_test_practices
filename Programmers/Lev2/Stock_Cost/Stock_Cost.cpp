#include <string>
#include <vector>
#include <iostream>
#include<stack>

using namespace std;


vector<int> solution(vector<int> prices) {
    int length = prices.size();

    vector<int> answer(length, 0);

    stack<pair<int, int>> my_stack;

    for (int current_index = 0; current_index < length; current_index++) {
        if (my_stack.size() < 1) {
            my_stack.push({ prices[current_index], current_index });
        }
        else {
            int t_last_index = my_stack.size()-1;
            pair<int, int> t_element = my_stack.top();
            
            while ((my_stack.size() > 0)& (t_element.first > prices[current_index])) {
                answer[t_element.second] = current_index - t_element.second;
                my_stack.pop();
                if (my_stack.size() > 0) {
                    t_element = my_stack.top();
                }
            }

            my_stack.push({ prices[current_index], current_index });
        }
    }

    while (my_stack.size() > 0) {
        pair<int, int> t_ele = my_stack.top();
        answer[t_ele.second] = (length - 1) - t_ele.second;
        my_stack.pop();
    }

    return answer;
}

int main() {
    vector<int> inputs = {5,5,3,3,4,3,1};

    vector<int> result = solution(inputs);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
   
}