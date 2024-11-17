import sys
input = sys.stdin.readline

N = int(input().strip())
cl = [list(map(int, input().split())) for _ in range(N)] 
st = [0] * N
same_class = [set() for _ in range(N)]

for i in range(5):
    sts = {}
    for j in range(N):
        cls = cl[j][i]
        sts.setdefault(cls, []).append(j)
    
    for cm in sts.values():
        for student in cm:
            for other in cm:
                if other != student and other not in same_class[student]:
                    same_class[student].add(other)
                    st[student] += 1

print(st.index(max(st)) + 1)