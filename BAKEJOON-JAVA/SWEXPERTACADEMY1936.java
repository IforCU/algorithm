import java.util.Scanner;

public class SWEXPERTACADEMY1936{
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();

        System.out.println((a - b + 3) % 3 == 1 ? "A" : "B");
    }
}