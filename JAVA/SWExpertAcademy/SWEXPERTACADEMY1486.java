package SWExpertAcademy;

import java.util.Scanner;

public class SWEXPERTACADEMY1486 {
    static int N, B, min;
    static int[] arr;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
		{
            N = sc.nextInt();
            B = sc.nextInt();
            arr = new int[N];

            for(int i = 0; i < N; i++) {
                arr[i] = sc.nextInt();
            }

            min = Integer.MAX_VALUE;
            backtrack(0, 0);

            System.out.println("#" + test_case + " " + min);
		}
    }
    
    static void backtrack(int idx, int sum) {
        if (sum >= B) {
            min = Math.min(min, sum - B);
            return;
        }
        if (idx == N) return;

        backtrack(idx + 1, sum + arr[idx]);
        backtrack(idx + 1, sum);
    }
}