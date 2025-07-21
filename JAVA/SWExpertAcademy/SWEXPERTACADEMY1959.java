package SWExpertAcademy;

import java.util.Scanner;

public class SWEXPERTACADEMY1959 {
   public static void main(String args[]) throws Exception{
        Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            int N = sc.nextInt();
            int M = sc.nextInt();
            int[] A = new int[N];
            int[] B = new int[M];
            for (int i = 0; i < N; i++) {
                A[i] = sc.nextInt();
            }
            for (int i = 0; i < M; i++) {
                B[i] = sc.nextInt();
            }

            int max = 0;
            if (N < M) {
                for (int i = 0; i <= M - N; i++) {
                    int sum = 0;
                    for (int j = 0; j < N; j++) {
                        sum += A[j] * B[i + j];
                    }
                    if (sum > max) {
                        max = sum;
                    }
                }
            } else {
                for (int i = 0; i <= N - M; i++) {
                    int sum = 0;
                    for (int j = 0; j < M; j++) {
                        sum += A[i + j] * B[j];
                    }
                    if (sum > max) {
                        max = sum;
                    }
                }
            }
            System.out.println("#" + test_case + " " + max);
		}
   }
}