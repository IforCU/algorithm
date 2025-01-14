from datetime import date

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

start = date(y1, m1, d1)
end = date(y2, m2, d2)

if y2 > y1 + 1000 or (y2 == y1 + 1000 and (m2, d2) >= (m1, d1)):
    print("gg")
else:
    print(f"D-{(end - start).days}")