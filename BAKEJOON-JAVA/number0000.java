import java.util.Scanner;
public class number0000 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] inputs = input.split(" "); // 입력 문자열을 공백으로 분할
        int a = Integer.parseInt(inputs[0]); // 첫 번째 숫자를 정수로 변환하여 a에 할당
        int b = Integer.parseInt(inputs[1]); // 두 번째 숫자를 정수로 변환하여 b에 할당
        int c = Integer.parseInt(inputs[2]); // 세 번째 숫자를 정수로 변환하여 c에 할당

        System.out.printf("%d %d %d",a,b,c);
    }
}