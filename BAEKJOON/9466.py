import sys
sys.setrecursionlimit(10**6)
T = int(input())
for _ in range(T):
    N = int(input())
    choice = [0] + list(map(int, input().split()))

    visited = [False] * (N+1)
    team_people = 0

    def dfs(i):
        global team_people
        visited[i] = True 
        team.append(i) 
        select = choice[i]  

        if visited[select]: 
            if select in team: 
                team_people += len(team[team.index(select):])
        else: 
            dfs(select)

    for i in range(1, N+1):
        if not visited[i]:
            team = []
            dfs(i)

    print(N - team_people)