package Lev2;

public class Matrix_Mul {

	public static void main(String[] args) {

		int[][] input1 = {{2, 3, 2},{4, 2, 4},{3, 1, 4}};
		int[][] input2 =  { {5, 4, 3}, {2, 4, 1}, {3, 1, 1}};
		
		// Expected : [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
		
		int[][] actual = solution(input1, input2);
		
		for(int i=0; i<actual.length; i++) {
			for(int j=0; j<actual[0].length; j++) {
				System.out.print(actual[i][j]+" ");
			}
			System.out.println();
		}
	}
	public static int[][] solution(int[][] arr1, int[][] arr2) {
        // C[i][j] = A[i][1]B[1][j] + A[i][2]B[2][j] + ... + A[i][n]*B[n][j]
        
        int num_x = arr1.length;
        int num_n = arr1[0].length;
        int num_y = arr2[0].length;
        
        int[][] answer = new int[num_x][num_y];
        
        for(int j=0; j<num_y; j++){
            for(int i=0; i<num_x; i++){
                answer[i][j] = 0;
                for(int t=0; t<num_n; t++){
                    answer[i][j] += arr1[i][t]*arr2[t][j];
                }
            }
        }
        return answer;
    }

}
