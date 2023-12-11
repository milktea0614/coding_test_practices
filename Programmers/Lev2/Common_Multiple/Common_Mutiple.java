package Lev2;

public class Common_Mutiple {

	public static void main(String[] args) {

		int result = 0;
		int [] arr = {2,6,8,14};
		
		result = solution(arr);
		System.out.println(result);

	}

	public static int solution(int[] arr) {
		int answer = 0;
		answer = arr[0];

		if (arr.length > 1) {
			for (int i = 1; i < arr.length; i++) {
				int temp = get_common_divisor(answer, arr[i]);
				answer = temp * (answer / temp) * (arr[i] / temp);
			}
		}

		return answer;
	}

	private static int get_common_divisor(int num1, int num2) {
		int small_num = num1;
		int big_num = num2;
		int result = 1;

		if (num1 > num2) {
			big_num = num1;
			small_num = num2;
		}

		for (int i = 1; i < Math.pow(small_num, 0.5) + 1; i++) {
			int mod = small_num % i;
			int div = small_num / i;

			if ((mod == 0) && (big_num % i == 0)) {
				result = i;
			}

			if ((small_num % div == 0) && (big_num % div == 0)) {
				if (result < div) {
					result = div;
					break;
				}
			}

		}

		return result;
	}
}
