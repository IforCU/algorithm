import sys
N = int(sys.stdin.readline())

word = []

for _ in range(N):
    word.append(sys.stdin.readline().strip())

word = list(set(word))
word.sort()
word.sort(key=len)

for ch in word:
    print(ch)