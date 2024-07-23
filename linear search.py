def linear_search(arr, target):
    for num in arr:
        if num == target:
            return "Exist"
    return "Not exist"

arr = [2, 4, 6, 8, 9, 7, 9]
target = 7
print(linear_search(arr, target))
target = 5
print(linear_search(arr, target))
