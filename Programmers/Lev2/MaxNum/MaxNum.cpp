#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(vector<int> numbers) {
    string answer = "";
    int count = numbers.size();
    int zero_count = 0;
    vector<string> temp(count);
    
	// string 로 바꾸기
    for(int i=0; i<count; i++){
    	temp[i] = to_string(numbers[i])+to_string(numbers[i])+to_string(numbers[i])+to_string(numbers[i]);
        if(numbers[i] ==0){
            zero_count+=1;
        }
    }
    
    if(zero_count == count){
        answer = "0";
    }else{
        sort(temp.begin(), temp.end()); 
        
        for(int i=count-1; i>=0; i--){
    	    int t_length = temp[i].length() / 4;
    	    string t_string = temp[i].substr(0,t_length);
    	    answer = answer+t_string;
        }
    }
    
    return answer;
}

int main(){
	vector<int> my_input = {10, 20, 30, 40, 50, 60, 70, 55}; //"7060555040302010"

	cout << solution(my_input) << "\n";

	return 0;
}