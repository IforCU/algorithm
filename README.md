# algorithm 공부를 위한 리포지토리

## 목표

- 백준 플래티넘을 목표로 하루 1 알고리즘을 풀도록 노력하기

## 자료구조

- set은 list를 조회하는 것보다 빠른 조회 성능을 가진다.
- ord()는 아스키 코드, chr() 숫자를 다시 문자로 97 = a
- 입력을 리스트로 받는 방법은 list(map(int,input().split()))
- 입력 빠르게 받는 방법은 import sys \n input = sys.stdin.readline

## 알고리즘

- list에서 가장 빠르게 탐색하는 기본적인 방법은 이진 탐색 트리이다.

```python
def binarySearch(arr,find):
    count = 0
    start = 0
    end = len(arr)

    while True:
        mid = (start + end) // 2

        if arr[mid] == find:
            break
        elif arr[mid] < find:
            start = mid -1
            count += 1
        else:
            end = mid + 1
            count += 1
    return count
```

- 동적 프로그래밍은 피보나치 수열, 최소 비용 경로, 배낭, 동전 교환, LIS 등 작은 문제를 풀면서 원하는 목적지까지 도달하는 문제에 적합하다.
  - 메모이제이션: 이미 계산한 값을 배열에 저장해서 중복 계산을 피하는 방법
  - 테이블 방식: 작은 값부터 차례대로 최소 값을 계산해 나가면서 배열에 결과를 저장하는 방식
- 메모이제이션(탑다운 방식)

```python
def fib(n, dp):
    if n == 0 or n == 1:
        return n
    if dp[n] != -1:
        return dp[n]

    dp[n] = fib(n-1, dp) + fib(n-2, dp)
    return dp[n]

n = 10
dp = [-1] * (n + 1)
print(fib(n, dp))
```

- 테이블 방식(바텀업 방식)

```python
def fib(n):
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

n = 10
print(fib(n))
```
