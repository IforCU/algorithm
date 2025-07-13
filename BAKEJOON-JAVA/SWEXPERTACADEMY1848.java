import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class SWEXPERTACADEMY1848 {
    static int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
    static int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};
    static int N;
    static char[][] map;
    static int[][] countMap;
    static boolean[][] visited;

    public static void main(String[] args) {
        Scanner sc  = new Scanner(System.in);
        int T = sc.nextInt();
        for(int test_case = 1; test_case <= T; test_case++)
		{
			N = sc.nextInt();
            map = new char[N][N];
            visited = new boolean[N][N];

            for(int i = 0; i < N; i++) {
                String str = sc.next();
                for(int j = 0; j < N; j++) {
                    map[i][j] = str.charAt(j);
                }
            }

            makeCountMap();

            int clicks = 0;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (countMap[i][j] == 0 && !visited[i][j]) {
                        clicks++;
                        bfs(i, j);
                    }
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (countMap[i][j] > 0 && !visited[i][j]) {
                        clicks++;
                    }
                }
            }

            System.out.println("#" + test_case + " " + clicks);
		}
    }

    static void makeCountMap() {
        countMap = new int[N][N];
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if(map[i][j] == '*') {
                    countMap[i][j] = -1;
                    continue;
                }

                int mineCount = 0;
                for(int d = 0; d < 8; d++) {
                    int nx = i + dx[d];
                    int ny = j + dy[d];
                    if(indexOfValid(nx, ny) && map[nx][ny] == '*') {
                        mineCount++;
                    }
                }
                countMap[i][j] = mineCount;
            }
        }
    }

    static boolean indexOfValid(int x, int y) {
        return x >= 0 && y >= 0 && x < N && y < N;
    }

    static void bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        visited[x][y] = true;

        while(!queue.isEmpty()) {
            int[] current = queue.poll();
            int curX = current[0];
            int curY = current[1];
            for(int d = 0; d < 8; d++) {
                int nx = curX + dx[d];
                int ny = curY + dy[d];
                if(indexOfValid(nx, ny) && !visited[nx][ny] && countMap[nx][ny] != -1) {
                    visited[nx][ny] = true;
                    if(countMap[nx][ny] == 0){
                        queue.add(new int[]{nx,ny});
                    }
                }
            }
        }
    }
}
