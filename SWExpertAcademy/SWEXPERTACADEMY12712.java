import java.util.Scanner;

public class SWEXPERTACADEMY12712 {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();
        for(int test_case = 1; test_case <= T; test_case++)
        {
            int N = sc.nextInt();
            int M = sc.nextInt();
            int max = 0;
            int[][] arr = new int[N][N];
            for (int i =0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    arr[i][j] = sc.nextInt();   
                }
            }
             
            for (int i =0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    int sumPlus = arr[i][j];
                    int sumX = arr[i][j];
                     
                    // + 
                    for (int k = 1; k < M; k++) { 
                        // ->
                        sumPlus += valid(i, j + k, N, arr);
                        // <-
                        sumPlus += valid(i, j - k, N, arr);
                        // 위
                        sumPlus += valid(i + k, j, N, arr);
                        // 아래
                        sumPlus += valid(i - k, j, N, arr);
                    }
                     
                    // x
                    for (int k = 1; k < M; k++) {
                        // 1시
                        sumX += valid(i + k, j + k, N, arr);
                        // 5시
                        sumX += valid(i - k, j + k, N, arr);
                        // 7시
                        sumX += valid(i - k, j - k, N, arr);
                        // 11시
                        sumX += valid(i + k, j - k, N, arr);
                    }
                     
                    max = Math.max(max, Math.max(sumPlus, sumX));
                }
            }
            System.out.println("#"+test_case+" "+max);
        }
    }
     
    public static int valid(int i, int j, int N, int[][] arr){
        if (i < 0 || i >= N || j < 0 || j >= N) return 0;
        else return arr[i][j];
    }
}
