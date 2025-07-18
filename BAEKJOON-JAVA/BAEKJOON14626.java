import java.util.Scanner;

public class BAEKJOON14626 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String isbn = sc.nextLine();

        int damagedIndex = -1;
        int sum = 0;

        for (int i = 0; i < isbn.length(); i++) {
            if (isbn.charAt(i) == '*') {
                damagedIndex = i;
                continue;
            }
            int digit = isbn.charAt(i) - '0';
            sum += digit * ((i % 2 == 0) ? 1 : 3);
        }

        int damagedWeight = (damagedIndex % 2 == 0) ? 1 : 3;

        for (int x = 0; x <= 9; x++) {
            if ((sum + x * damagedWeight) % 10 == 0) {
                System.out.println(x);
                break; 
            }
        }
    }
}
