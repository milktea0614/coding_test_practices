package Lev2;

import java.util.*;

class My_Pair{
	int value;
	int index;
	
	My_Pair(int p_value, int p_index){
		value = p_value;
		index = p_index;
	}
}

public class Stock_Cost {
	
	public static void main(String[] args) {
		int[] inputs = {5,5,3,3,4,3,1}; // [2, 1, 4, 3, 1, 1, 0]
		
		int[] result = solution(inputs);
		
		for(int i=0; i<result.length; i++) {
			System.out.print(result[i]+" ");
		}
		System.out.println();

	}

	public static int[] solution(int[] prices) {
		int length = prices.length;
		
        int[] answer = new int[length];
        
        // 0으로 초기화
        for(int i=0; i<length; i++) {
        	answer[i] = 0;
        }
        
        // Stack 생성
        Stack<My_Pair> my_stack = new Stack<>();
        
        for(int current=0; current<length; current++) {
        	if(my_stack.size() < 1) {
        		my_stack.add(new My_Pair(prices[current], current));
        	}else {
        		My_Pair t_element = my_stack.peek();
        		
        		while((my_stack.size() > 0) && (t_element.value > prices[current])) {
        			answer[t_element.index] = current - t_element.index;
        			
        			my_stack.pop();
        			if(my_stack.size() > 0) {
        				t_element = my_stack.peek();
        			}
        		}
        		
        		my_stack.add(new My_Pair(prices[current], current));
        	}
        }
        
        while(my_stack.size() > 0) {
        	My_Pair temp = my_stack.pop();
        	answer[temp.index] = (length-1)-temp.index;
        }

        
        return answer;
    }
}
