n = 999
exclude = set([13])

# "13"이 포함된 숫자를 구합니다.
exclude_set = set()
for num in range(1, n + 1):
    if "13" in str(num):
        exclude_set.add(num)
exclude |= exclude_set

# "13"이 포함되지 않은 숫자를 구합니다.
nums = set(range(1, n + 1)) - exclude

# 결과 출력
print(len(nums))