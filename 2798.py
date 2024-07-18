N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards.sort()
n = len(cards)
closest_sum = 0

for i in range(n - 2):
    left, right = i + 1, n - 1
    while left < right:
        current_sum = cards[i] + cards[left] + cards[right]
        
        if current_sum <= M:
            if current_sum > closest_sum:
                closest_sum = current_sum
            left += 1
        else :
            right -= 1

print(closest_sum)