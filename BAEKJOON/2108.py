N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

count = [0] * len(numbers)

set_list = set(numbers)
max_count = 0
for i in set_list:
    count = numbers.count(i)
    if max_count < count:
        max_count = count
answer = []
for i in set_list:
    count = numbers.count(i)
    if(max_count == count):
        answer.append(i)
answer.sort()


# 결과 출력
print(round(sum(numbers) / N))
print(numbers[N//2])
if(len(answer) == 1):
    print(answer[0])
else:
    print(answer[1])
print(numbers[-1] - numbers[0])
