import time

# 테스트 데이터
n = 100000  # 문자열 길이
data = ["a"] * n  # "a"를 n번 반복한 리스트

# 1. `+=` 방식
start = time.time()
result = ""
for char in data:
    result += char
end = time.time()
print(f"Using +=: {end - start:.5f} seconds")

# 2. 리스트 + `join()` 방식
start = time.time()
result = "".join(data)
end = time.time()
print(f"Using join(): {end - start:.5f} seconds")
