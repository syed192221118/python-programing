def count_occurrences(numbers, target):
    return numbers.count(target)

numbers = (3, 6, 8, 9, 8, 9, 12, 35, 8)
target = 8
print(count_occurrences(numbers, target))  # Output: 3
