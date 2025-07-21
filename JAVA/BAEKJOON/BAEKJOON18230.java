package BAEKJOON;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class BAEKJOON18230 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int A = sc.nextInt();
        int B = sc.nextInt();
        int sum = 0;

        Integer[] tiles_A = new Integer[A];
        Integer[] tiles_B = new Integer[B];

        for (int i = 0; i < A; i++) {
            tiles_A[i] = sc.nextInt();
        }

        for (int i = 0; i < B; i++) {
            tiles_B[i] = sc.nextInt();
        }

        Arrays.sort(tiles_A, Collections.reverseOrder());
        Arrays.sort(tiles_B, Collections.reverseOrder());

        int[] prefix_A = new int[A + 1];
        int[] prefix_B = new int[B + 1];

        for (int i = 1; i <= A; i++) prefix_A[i] = prefix_A[i - 1] + tiles_A[i - 1];
        for (int i = 1; i <= B; i++) prefix_B[i] = prefix_B[i - 1] + tiles_B[i - 1];

        for (int k = 0; k <= B; k++) {
            int areaUsed = 2 * k;
            if (areaUsed > N) continue;

            int oneTileNeeded = N - areaUsed;
            if (oneTileNeeded > A) continue;

            int beauty = prefix_B[k] + prefix_A[oneTileNeeded];
            sum = Math.max(sum, beauty);
        }

        System.out.println(sum);
    }
}