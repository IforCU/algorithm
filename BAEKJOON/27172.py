from math import isqrt

def calculate_scores(N, cards):
    scores = {card: 0 for card in cards}

    max_card = max(cards)
    is_prime = [True] * (max_card + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, isqrt(max_card) + 1):
        if is_prime[i]:
            for multiple in range(i*i, max_card + 1, i):
                is_prime[multiple] = False
    
    for card in cards:
        for multiple in range(2*card, max_card + 1, card):
            if multiple in scores:
                scores[card] += 1
                scores[multiple] -= 1

    return [scores[card] for card in cards]

N = int(input())
cards = list(map(int, input().split()))

ans = calculate_scores(N, cards)
print(" ".join(map(str, ans)))