digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

NFormation, BFormation = map(int,input().split())
ans = ""

while NFormation > 0:
    ans += digits[NFormation % BFormation]
    NFormation //= BFormation

print(ans)