N = int(input())
books = dict()
for _ in range(N):
    str = input()
    if str in books:
        books[str] += 1
    else:
        books[str] = 1

value = max(books.values())
arr = []
for k, v in books.items():
    if v == value:
        arr.append(k)

arr.sort()
print(arr[0])
