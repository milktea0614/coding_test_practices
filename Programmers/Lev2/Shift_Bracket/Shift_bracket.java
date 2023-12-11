package Shift_bracket;

public class Shift_bracket {

	public static void main(String[] args) {
		String[] my_input = {"[](){}", "}]()[{", "[)(]", "}}}"}; // 3, 2, 0, 0
		
		for(int i=0; i<my_input.length; i++) {
			System.out.println(solution(my_input[i]));
		}

	}
	
	public static int solution(String s) {
        int answer = 0;
        
        for(int i=0; i<s.length(); i++) {
        	answer += check_correct_string(s);
        	s = shift_left_string(s);
        }
        
        return answer;
    }

	private static String shift_left_string(String p_s){
        String result = "";
        
        if (p_s.length() > 1) {
        	result = p_s.substring(1)+p_s.charAt(0);
        }else {
        	result = p_s;
        }
		return result;
    }
	
    private static int check_correct_string(String p_s){
        int max_count = (p_s.length() / 2) +1;
        for(int i=0; i<max_count; i++) {
        	String temp1 = p_s.replace("()", "");
        	String temp2 = temp1.replace("[]", "");
        	p_s = temp2.replace("{}", "");

        	if(p_s.length() == 0) {
        		break;
        	}
        }

        if (p_s.length() > 0) {
        	return 0;
        }else {
        	return 1;
        }
    }
}
