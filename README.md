# algorithm 공부를 위한 리포지토리

## 목표

- 백준 플래티넘을 목표로 하루 1 알고리즘을 풀도록 노력하기

## 자료구조

- set은 list를 조회하는 것보다 빠른 조회 성능을 가진다.
- ord()는 아스키 코드, chr() 숫자를 다시 문자로 97 = a
- 입력 빠르게 받는 방법은

```python
import sys
input = sys.stdin.readline
maps = list(map(int,input().split())) # 입력을 리스트로 받는 방법 (int)
```

### heap은 특정한 규칙을 가지는 트리로, 최댓값과 최솟값을 찾는 연산을 빠르게 하기위해 고안된 완전 이진트리를 기본으로 함.

- 파이썬에서 `heapq` 라는 라이브러리를 제공함

```python
import heapq

heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap) # [10, 50, 20]

print(heapq.heappop(heap)) # 10 [20, 50]
print(heap[0]) # 20 [20, 50]
```

- heapq을 최대 값 정렬로 바꿀려면 튜플 형태로 값을 넣어서 값이 커지면 음수 값도 커지니 우선 정렬로 바뀌는 성질을 이용하면 된다.

```python
heap_items = [1,3,5,7,9]

max_heap = []
for item in heap_items:
  heapq.heappush(max_heap, (-item, item))

print(max_heap) # [(-9, 9), (-7, 7), (-3, 3), (-1, 1), (-5, 5)]
```

## 알고리즘

### list에서 가장 빠르게 탐색하는 기본적인 방법은 이진 탐색 트리이다.

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

### 동적 프로그래밍은 피보나치 수열, 최소 비용 경로, 배낭, 동전 교환, LIS 등 작은 문제를 풀면서 원하는 목적지까지 도달하는 문제에 적합하다.

- 동적 프로그래밍 알고리즘을 만들때는 가장 중요한 점이 점화식을 만들어 내는 것이다. f(n) = f(n-1) + f(n-2) 등
- 메모이제이션: 이미 계산한 값을 배열에 저장해서 중복 계산을 피하는 방법
- 테이블 방식: 작은 값부터 차례대로 최소 값을 계산해 나가면서 배열에 결과를 저장하는 방식

#### 메모이제이션(탑다운 방식)

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

#### 테이블 방식(바텀업 방식)

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

### 그래프 탐색은 Node, link 관계로 이루어져 있으며, 2차원 배열을 활용해 node가 연결된 값을 확인할 수 있다.

- 다음과 같이 node를 만든다.

```python
N, M = map(int, input().split()) # M = node, N = link
node = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    node[x].append(y)
    node[y].append(x)
print(node) # [[],[2,3],[1,3][1,2]]
```

### 이런 상황에서 node를 빠르게 탐색하는 방법은 DFS와 BFS 방식이 있다.

#### DFS 방식은 재귀를 이용해 가장 깊은 곳까지 탐색하는 방법으로 스택이 깊은 곳까지 쌓이기 때문에 조심해야된다.

```python
visited = [False] * (N+1)
def dfs(node,v):
    visited[v] = True
    for i in node[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
            visited[i] = False
```

#### BFS 방식은 queue를 활용하여 얇은 곳부터 전부를 확인하면서 들어가는 탐색 방법으로 반복문을 사용한다.

```python
visited = [False] * (N+1)
def bfs(node,v):
    queue = deque([v])
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in node[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
```

### 이진 Tree는 딕셔너리로 구현하는게 가장 편하고 빠르다.

- **preOrder**는 root를 먼저 방문한다.
- **inOrder**는 왼쪽 하위 트리를 방문 후 root를 방문
- **postOrder**는 하위 트리 모두 방문 후 root를 방문

```python
tree = {} # dict 자료구조

for n in range(N):
    root, left, right = input().rstrip().split()
    tree[root] = [left, right] # root에 left, right를 넣어 이진 트리 완성

def preOrder(root): # 출력이 먼저(pre)
    if root != '.':
        print(root, end='')
        preOrder(tree[root][0])
        preOrder(tree[root][1])

def inOrder(root): # 출력이 중간 (in)
    if root != '.':
        inOrder(tree[root][0])
        print(root, end='')
        inOrder(tree[root][1])

def postOrder(root): # 출력이 마지막 (post)
    if root != '.':
        postOrder(tree[root][0])
        postOrder(tree[root][1])
        print(root, end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
```

### 문자열 처리 방식 += VS join()

- += 로 문자열을 처리하는 것 보다는 list를 이용해 join을 사용하는것이 훨씬 성능이 좋다.
- Python에서 문자열은 불변 객체임으로 += 수행을 시작하면 다음과 같다
  - 새로운 문자열 객체사 생성
  - 기존 문자열의 내용을 새 객체로 복사
  - 매번 문자열의 크기 만큼 복사 비용이 발생하므로 O(n^2)의 성능을 보여준다

```Python
import time
n = 100000
data = ["a"] * n

start = time.time()
result = ""

for char in data:
    result += char
end = time.time()
print(f"Using +=: {end - start:.5f} seconds")

start = time.time()
result = "".join(data)
end = time.time()
print(f"Using join(): {end - start:.5f} seconds")

# 결과
# Using +=: 0.09099 seconds -> O(n^2)
# Using join(): 0.00051 seconds -> O(n)
```
