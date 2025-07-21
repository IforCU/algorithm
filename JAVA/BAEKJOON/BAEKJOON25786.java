package BAEKJOON;
import java.util.Scanner;

public class BAEKJOON25786 {
    public void solution() throws Exception {
        Scanner sc = new Scanner(System.in);
        String num1 = sc.nextLine();
        String num2 = sc.nextLine();

        int maxLength = Math.max(num1.length(), num2.length());
        num1 = String.format("%" + maxLength + "s", num1).replace(' ', '0');
        num2 = String.format("%" + maxLength + "s", num2).replace(' ', '0');

        StringBuilder result = new StringBuilder();
        
        for (int i=0; i < maxLength; i++) {
            int digit1 = num1.charAt(i) - '0';
            int digit2 = num2.charAt(i) - '0';
            
            if((digit1 <= 2 && digit2 <= 2) || (digit1 >= 7 && digit2 >= 7)) {
                result.append('0');
            } else {
                result.append('9');
            }
        }

        System.out.println(result);
    }
}
