package SWExpertAcademy;

import java.util.Scanner;

public class SWEXPERTACADEMY1206 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = 10;
        
        for (int test_case = 1; test_case <= T; test_case++) {
            int N = sc.nextInt();
            int[] arr = new int[N];
            int sum = 0;
            for (int i = 0; i < N; i++) {
                arr[i] = sc.nextInt();
            }

            for (int i = 2; i < N-2; i++) {
                int max = 0;
                for (int j = -2; j <= 2; j++) {
                    if (j == 0) continue;
                    max = Math.max(max, arr[i + j]);
                }
                if (arr[i] > max) {
                    sum += arr[i] - max;
                }
            }

            System.out.println("#" + test_case + " " + sum);
        }
    }
}
