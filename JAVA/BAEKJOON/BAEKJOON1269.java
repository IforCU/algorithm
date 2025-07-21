package BAEKJOON;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class BAEKJOON1269 {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();

        Set<Integer> setA = new HashSet<>();
        Set<Integer> setB = new HashSet<>();

        for (int i = 0; i < A; i++) {
            setA.add(sc.nextInt());
        }

        for (int i = 0; i < B; i++) {
            setB.add(sc.nextInt());
        }

        Set<Integer> A_diff = new HashSet<>(setA);
        A_diff.removeAll(setB);
        Set<Integer> B_diff = new HashSet<>(setB);
        B_diff.removeAll(setA); 

        A_diff.addAll(B_diff); 
        System.out.println(A_diff.size());
    }
}