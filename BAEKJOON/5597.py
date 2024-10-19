import sys
input = sys.stdin.readline
students = {}
for _ in range(28):
    students[int(input())] = 1

for i in range(1,31):
    if students.get(i,0) == 0:
        print(i)