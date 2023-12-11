#include <iostream>

#include <string>
#include <vector>

using namespace std;

string replaceAll(string change, string target, string original){
	int change_length = change.length();
	int target_length = target.length();
	int index = 0;
	
	string result = original;
	
	while ((index = result.find(target)) != string::npos){
		result.replace(index, target_length, change);
		index = result.find(target);
	}
	
	return result;
}
string shift_left_string(string p_s){
	int string_length = p_s.length();
	string result = "";
	
	if (string_length > 1){
		char first = p_s[0];
		result = p_s.substr(1);
		result = result+first;
	}
	else{
		result = p_s;
	}
	return result;
}

int check_correct_string(string p_s){
	int string_length = p_s.length();
	
	for(int i=0; i<(string_length /2)+1;i++){
		string temp1 = replaceAll("","()",p_s);
		string temp2 = replaceAll("", "[]",temp1);
		p_s = replaceAll("", "{}",temp2);
	}
	
	if (p_s.length() > 0){
		return 0;
	}else{
		return 1;
	}
}

int solution(string s) {
    int answer = 0;
    int string_length = s.length();
    
    if (string_length % 2 > 0){
    	answer = 0;
    }
    else{
    	for(int i=0; i<string_length; i++){
    		answer += check_correct_string(s);
    		s = shift_left_string(s);
    	}
    }
   
    return answer;
}

int main(){
	vector<string> my_input = {"[](){}", "}]()[{", "[)(]", "}}}"}; // 3, 2, 0, 0
	
	for(int i=0; i<my_input.size(); i++){
		cout << solution(my_input[i]) << "\n";
	}
	
	return 0;
}
