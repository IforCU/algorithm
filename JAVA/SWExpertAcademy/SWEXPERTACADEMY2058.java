package SWExpertAcademy;

import java.util.Scanner;

public class SWEXPERTACADEMY2058 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        String N = sc.nextLine();
        int sum = 0;
        for (int i = 0; i < N.length(); i++) {
            char c = N.charAt(i);
            sum += c - '0';
        }
        System.out.println(sum);
    }
}