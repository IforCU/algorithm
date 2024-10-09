import sys
input = sys.stdin.readline
N, M = map(int, input().split())
passwords = {}
for _ in range(N):
    site, password = map(str, input().rstrip().split())
    passwords[site] = password

for _ in range(M):
    site = input().rstrip()
    print(passwords.get(site))