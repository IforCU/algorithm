N = int(input())
my_string = input()

for _ in range(N - 1):
    s = input()
    for j in range(len(s)):
        if my_string[j] != s[j]:
            my_string = my_string[:j] + '?' + my_string[j + 1:]

print(my_string)
