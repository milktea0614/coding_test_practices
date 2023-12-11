#include <string>
#include <vector>
#include <math.h>
#include <iostream>
using namespace std;

int get_common_divisor(int num1, int num2){
    int small_num = num1;
    int big_num = num2;
    int result = 1;
    
    if(num1 > num2){
        small_num = num2;
        big_num = num1;
    }
    
    for(int i=1; i< int(pow(small_num, 0.5)+1);i++){
        int div = small_num / i;
        int mod = small_num % i;
        if((mod == 0) && (big_num % i == 0)){
            result = i;
        }
        if((small_num % div == 0) && (big_num % div == 0)){
            if(result < div){
                result = div;
                break;
            }
        }
    }
    return result;
}

int solution(vector<int> arr) {
    int answer = 0;
    int length = arr.size();
    
    answer = arr[0];
    
    for(int i=1;i<length;i++){
        int common_divisor = get_common_divisor(answer, arr[i]);
        int div1 = answer / common_divisor;
        int div2 = arr[i] / common_divisor;
        
        answer = common_divisor * (div1) * (div2);
    }
    return answer;
}

int main(){
	vector<int> my_input = {2,6,8,14}; // 168

	cout << solution(my_input) << "\n";

	return 0;
}
