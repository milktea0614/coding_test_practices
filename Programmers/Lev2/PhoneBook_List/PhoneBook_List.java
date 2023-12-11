package Lev2;
import java.util.*;

public class PhoneBook_List {

	public static void main(String[] args) {
		String[] t_input = {"119", "97674223", "1195524421"};
		
		System.out.println(solution(t_input));

	}
	
	public static boolean solution(String[] phone_book) {
        boolean answer = true;
        
        Arrays.sort(phone_book);
        
        for(int i=0; i<(phone_book.length-1); i++){
int current_str_length = phone_book[i].length();
            
            if(current_str_length <= phone_book[i+1].length()){
                String next_str = phone_book[i+1].substring(0, current_str_length);
            
                if(next_str.equals(phone_book[i])){
                    answer = false;
                    break;
                }
            }
        }
        return answer;
    }

}
