# 아래 함수를 수정하시오.
def find_min_max(numbers):
    min_val = numbers[0]
    max_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            maz_val = num
    return min_val, max_val

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
