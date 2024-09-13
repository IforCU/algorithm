N, K = map(int, input().split())
peo = [i for i in range(1, N+1)] # N 크기의 배열 생성

pt = 0 # Point가 될 값
ans = [] # ans 가 될 값
for _ in range(N):
    pt += K-1 # pt는 N-1만큼 움직인다
    pt %= len(peo) # pt는 현재 peo의 크기를 넘을 수 없음
    ans.append(peo.pop(pt)) # pt에 위치한 수를 삭제하면서 ans에 넣음

print(f"<{ ', '.join(map(str, ans))}>") # 답을 출력