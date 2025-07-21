package SWExpertAcademy;

import java.util.Scanner;
import java.util.Queue;

public class SWEXPERTACADEMY4193 {

    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int N;
    static int x, y;
    static int targetX, targetY;
    static int[][] map;
    static boolean[][][] visited;
    
    static class Point {
        int x, y, time;
        
        Point(int x, int y) {
            this.x = x;
            this.y = y;
            this.time = 0;
        }
        
        Point(int x, int y, int time) {
            this.x = x;
            this.y = y;
            this.time = time;
        }
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        for (int test_case = 1; test_case <= T; test_case++) {
            N = sc.nextInt();
            map = new int[N][N];
            visited = new boolean[N][N][3];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    map[i][j] = sc.nextInt();
                }
            }

            x = sc.nextInt();
            y = sc.nextInt();
            targetX = sc.nextInt();
            targetY = sc.nextInt();
            int answer = bfs(x, y, targetX, targetY);

            System.out.println("#" + test_case + " " + answer);
            
        }
    }

    static int bfs(int startX, int startY, int targetX, int targetY) {
        Queue<Point> queue = new java.util.LinkedList<>();

        visited = new boolean[N][N][3];
    
        queue.offer(new Point(startX, startY, 0));
        visited[startX][startY][0] = true;
    
        while (!queue.isEmpty()) {
            Point current = queue.poll();
            int cx = current.x;
            int cy = current.y;
            int time = current.time;
    
            if (cx == targetX && cy == targetY) {
                return time;
            }
    
            int nextTime = time + 1;
            int nextTimeMod = nextTime % 3;
    
            if (!visited[cx][cy][nextTimeMod]) {
                visited[cx][cy][nextTimeMod] = true;
                queue.offer(new Point(cx, cy, nextTime));
            }
    
            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
    
                if (!isValid(nx, ny) || map[nx][ny] == 1) {
                    continue;
                }
    
                if (map[nx][ny] == 2 && time % 3 != 2) {
                    continue;
                }
    
                if (!visited[nx][ny][nextTimeMod]) {
                    visited[nx][ny][nextTimeMod] = true;
                    queue.offer(new Point(nx, ny, nextTime));
                }
            }
        }
        return -1;
    }

    static boolean isValid(int x, int y) {
        return x >= 0 && x < N && y >= 0 && y < N;
    }
}