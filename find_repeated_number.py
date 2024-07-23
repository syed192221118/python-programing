def find_repeated_number(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)

arr = [1, 3, 4, 2, 2]
print(find_repeated_number(arr))
