package BAEKJOON;
import java.util.Scanner;

public class BAEKJOON11059{
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        
        int n = input.length();
        int maxLen = 0;

        int[] prefixSum = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            prefixSum[i] = prefixSum[i - 1] + (input.charAt(i - 1) - '0');
        }

        for (int len = 2; len <= n; len += 2) {
            for (int i = 0; i + len <= n ; i++) {
                int mid = i + len / 2;
                int sum1 = prefixSum[mid] - prefixSum[i];
                int sum2 = prefixSum[i + len] - prefixSum[mid];
                if(sum1 == sum2) {
                    maxLen = Math.max(maxLen, len);
                }
            }
        }
        
        System.out.println(maxLen);
    }
}