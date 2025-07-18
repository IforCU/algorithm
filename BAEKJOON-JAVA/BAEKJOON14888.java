import java.util.Scanner;

public class BAEKJOON14888 {
    static int N;
    static int[] numbers;
    static int[] operators;
    static int[] operatorsCount;
    static int max = Integer.MIN_VALUE;
    static int min = Integer.MAX_VALUE;
    static boolean[] visited;

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        numbers = new int[N];
        visited = new boolean[N-1];
        operatorsCount = new int[N-1];

        for (int i = 0; i < N - 1; i++) {
            operatorsCount[i] = -1; 
        }

        for (int i = 0; i < N; i ++) {
            numbers[i] = sc.nextInt();
        }

        operators = new int[4];
        for (int i = 0; i < 4; i++) {
            operators[i] = sc.nextInt();
        }

        backtrack(0);
        System.out.println(max);
        System.out.println(min);

        sc.close(); // for commit
    }

    public static void backtrack(int depth) {
        if (depth == N -1) {
            int result = numbers[0];
            for (int i = 0; i < N - 1; i++) {
                if (operatorsCount[i] == 0) {
                    result += numbers[i + 1];
                } else if (operatorsCount[i] == 1) {
                    result -= numbers[i + 1];
                } else if (operatorsCount[i] == 2) {
                    result *= numbers[i + 1];
                } else if (operatorsCount[i] == 3) {
                    if (result < 0) {
                        result = -(-result / numbers[i + 1]);
                    } else {
                        result /= numbers[i + 1];
                    }
                }
            }
            max = Math.max(max, result);
            min = Math.min(min, result);
            return;
        }
        
        for (int i = 0; i < 4; i++) {
            if (operators[i] > 0) {
                operatorsCount[depth] = i;
                operators[i]--;
                visited[depth] = true;
                backtrack(depth + 1);
                operatorsCount[depth] = -1;
                operators[i]++;
                visited[depth] = false;
            }
        }
        return;
    }
}