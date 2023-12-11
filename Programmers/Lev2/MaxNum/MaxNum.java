package Lev2;

import java.util.Arrays;

public class MaxNum {

	public static void main(String[] args) {
		int[] my_input = {10, 20, 30, 40, 50, 60, 70, 55}; //"7060555040302010"
		
		System.out.println(solution(my_input));
	}

	public static String solution(int[] numbers) {
        String answer = "";
        int length = numbers.length;
        int zero_count = 0;
        
        String[] num_string = new String[length];
        
        // int -> String array
        for(int i=0; i<length; i++) {
        	if(numbers[i] == 0) {
        		zero_count++;
        	}
        	String temp = Integer.toString(numbers[i]);
        	num_string[i] = temp+temp+temp+temp;
        }
        
        if(zero_count == length) {
        	answer = "0";
        }else {
        	Arrays.sort(num_string);
        	for(int i=length-1; i>=0; i--) {
        		int t_length = num_string[i].length() / 4;
        		String original = num_string[i].substring(0, t_length);
        		answer = answer + original;
        	}
        }
        return answer;
    }
}
