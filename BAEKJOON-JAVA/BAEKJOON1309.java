import java.util.Scanner;

public class BAEKJOON1309 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] dp = new int[N][3];
        int MOD = 9901;

        dp[0][0] = 1; 
        dp[0][1] = 1; 
        dp[0][2] = 1; 

        for (int i = 1; i < N; i++) {
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD;
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD; 
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % MOD; 
        }

        int result = (dp[N-1][0] + dp[N-1][1] + dp[N-1][2]) % MOD;
        System.out.println(result);
    }   
}