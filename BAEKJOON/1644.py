n = int(input())

def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(limit + 1) if sieve[i]]

def count_primes(n):

    primes = generate_primes(n)
    left, right = 0, 0
    current_sum = 0
    count = 0

    while right < len(primes):
        if current_sum < n:
            current_sum += primes[right]
            right += 1
        elif current_sum > n:
            current_sum -= primes[left]
            left += 1
        else:
            count += 1
            current_sum -= primes[left]
            left += 1

    if n in primes:
        count += 1

    return count

print(count_primes(n))