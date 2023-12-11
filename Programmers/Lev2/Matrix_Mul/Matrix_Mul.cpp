#include<string>
#include<vector>
#include<iostream>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    // C[i][j] = A[i][1]B[1][j] + A[i][2]B[2][j] + ... + A[i][n]*B[n][j]

    int num_x = arr1.size();
    int num_n = arr1[0].size();
    int num_y = arr2[0].size();

    // answer init
    vector<int> temp(num_y); // 0으로 채워진 1차원 배열
    vector<vector<int>> answer(num_x, temp);

    for (int j = 0; j < num_y; j++) {
        for (int i = 0; i < num_x; i++) {
            for (int t = 0; t < num_n; t++) {
                answer[i][j] = answer[i][j] + (arr1[i][t] * arr2[t][j]);
                
            }
        }
    }
    return answer;
}

int main() {

    /*
    vector<vector<int>> input1 = { {1, 4}, {3, 2}, {4, 1} };
    vector<vector<int>> input2 = { {3, 3}, {3, 3} };

    // Expected : [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
    */
    
    vector<vector<int>> input1 = {{2, 3, 2},{4, 2, 4},{3, 1, 4}};
    vector<vector<int>> input2 = { {5, 4, 3}, {2, 4, 1}, {3, 1, 1}};

    // Expected : [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
    
    vector<vector<int>> t_result = solution(input1, input2);
    
    for (int i = 0; i < t_result.size(); i++) {
        for (int j = 0; j < t_result[0].size(); j++) {
            cout << t_result[i][j] << " ";
        }
        cout << "\n" << endl;
    }
}