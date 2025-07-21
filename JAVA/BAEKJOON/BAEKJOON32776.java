package BAEKJOON;
import java.util.Scanner;

public class BAEKJOON32776 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int S = sc.nextInt();
        int N = sc.nextInt() + sc.nextInt() + sc.nextInt();

        if (S <= N || S <= 240 ) {
            System.out.println("high speed rail");
        } else {
            System.out.println("flight");
        }
    }
}