package BAEKJOON;
import java.util.Scanner;

public class BAEKJOON14503 {
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int N, M;
    static int[][] map;
    static int robotX, robotY, robotDir;
    static int cleanedCount = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        map = new int[N][M];

        robotX = sc.nextInt();
        robotY = sc.nextInt();
        robotDir = sc.nextInt();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                map[i][j] = sc.nextInt();
            }
        }

        clean();
        System.out.println(cleanedCount);
        sc.close();
    }  
    
    public static void clean() {
        while(true) {
            if (map[robotX][robotY] == 0) {
                map[robotX][robotY] = 2; 
                cleanedCount++;
            }

            boolean cleaned = false;

            int originalDir = robotDir;

            for (int i = 0; i < 4; i++) {
                robotDir = (robotDir + 3) % 4; 
                int nextX = robotX + dx[robotDir];
                int nextY = robotY + dy[robotDir];

                if (isValid(nextX, nextY) && map[nextX][nextY] == 0) {
                    robotX = nextX;
                    robotY = nextY;
                    cleaned = true;
                    break;
                }
            }

            if (cleaned) {
                continue;
            }

            robotDir = originalDir;
            int backX = robotX - dx[robotDir];
            int backY = robotY - dy[robotDir];

            if (isValid(backX, backY) && map[backX][backY] != 1) {
                robotX = backX;
                robotY = backY;
            } else {
                break; 
            }
        }
    }

    public static boolean isValid(int x, int y) {
        return x >= 0 && x < N && y >= 0 && y < M && map[x][y] != 1;
    }
}
