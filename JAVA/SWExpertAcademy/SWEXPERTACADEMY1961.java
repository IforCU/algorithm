package SWExpertAcademy;

import java.util.Scanner;

public class SWEXPERTACADEMY1961 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();
        
        for(int test_case = 1; test_case <= T; test_case++)
        {
            int N = sc.nextInt();
            int[][] arr = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }
             
            System.out.println("#" + test_case);
             
            for (int i = 0; i < N; i++) {
                // 90
                for (int j = N-1; j >=0; j--) {
                    System.out.print(arr[j][i]);
                }
                System.out.print(" ");
                // 180
                for (int j = N-1; j >=0; j--) {
                    System.out.print(arr[N-1-i][j]);
                }
                System.out.print(" ");
                 
                //270
                for (int j = 0; j < N; j++) {
                    System.out.print(arr[j][N-1-i]);
                }
                System.out.print(" ");
                 
                System.out.println();
            }
        }
    }
}
