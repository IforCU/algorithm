import java.util.Arrays;
import java.util.Scanner;

public class BAEKJOON26091{
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);

        int left = 0;
        int right = N - 1;
        int result = 0;
        while (left < right) {
            int sum = arr[left] + arr[right];
            if (sum < M) left++;
            else {
                result++;
                left++;
                right--;
            }
            
        }
        System.out.println(result);
    }
}