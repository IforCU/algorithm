package SWExpertAcademy;

import java.util.Scanner;

public class SWEXPERTACADEMY1873 {
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int dir = 0;
    static char[] directions = {'^', 'v', '<', '>'};
    static char[][] map;
    static int H, W, N;
    static String commands;
    static Point tank;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        for (int test_case = 1; test_case <= T; test_case++) {
            H = sc.nextInt();
            W = sc.nextInt();
            map = new char[H][W];

            for (int i = 0; i < H; i++) {
                String line = sc.next();
                for (int j = 0; j < W; j++) {
                    if (line.charAt(j) == '^') {
                        tank = new Point(i, j, 0);
                        map[i][j] = '.';
                    } else if (line.charAt(j) == 'v') {
                        tank = new Point(i, j, 1);
                        map[i][j] = '.';
                    } else if (line.charAt(j) == '<') {
                        tank = new Point(i, j, 2);
                        map[i][j] = '.';
                    } else if (line.charAt(j) == '>') {
                        tank = new Point(i, j, 3);
                        map[i][j] = '.';
                    } else {
                        map[i][j] = line.charAt(j);
                    }
                }
            }

            N = sc.nextInt();
            commands = sc.next();

            start();

            System.out.print("#" + test_case + " ");
            for (int i = 0; i < H; i++) {
                for (int j = 0; j < W; j++) {
                    if (i == tank.x && j == tank.y) {
                        System.out.print(directions[tank.dir]);
                    } else {
                        System.out.print(map[i][j]);
                    }
                }
                System.out.println();
            }
        }
        sc.close();
    }

    static void start() {
        for (char command : commands.toCharArray()) {
            switch (command) {
                case 'U':
                    tank.dir = 0;
                    move();
                    break;
                case 'D':
                    tank.dir = 1;
                    move();
                    break;
                case 'L':
                    tank.dir = 2;
                    move();
                    break;
                case 'R':
                    tank.dir = 3;
                    move();
                    break;
                case 'S':
                    shoot();
                    break;
            }
        }

    }

    static class Point {
        int x, y, dir;

        Point(int x, int y, int dir) {
            this.x = x;
            this.y = y;
            this.dir = dir;
        }
    }
    
    static boolean isValid(int x, int y) {
        return x >= 0 && x < H && y >= 0 && y < W;
    }   

    static void move() {
        int nx = tank.x + dr[tank.dir];
        int ny = tank.y + dc[tank.dir];

        if (isValid(nx, ny) && map[nx][ny] == '.') {
            tank.x = nx;
            tank.y = ny;
        }
    }

    static void shoot() {
        int nx = tank.x;
        int ny = tank.y;

        while (true) {
            nx += dr[tank.dir];
            ny += dc[tank.dir];

            if (!isValid(nx, ny)) break;
            if (map[nx][ny] == '#') break; 
            if (map[nx][ny] == '*') {
                map[nx][ny] = '.'; 
                break;
            }
        }
    }
}