digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

NFormation, BFormation = map(int,input().split())
ans = ""
if NFormation == 0:
    ans = "0"
else:
    ans = ""

    while NFormation > 0:
        ans = digits[NFormation % BFormation] + ans
        NFormation //= BFormation

print(ans)