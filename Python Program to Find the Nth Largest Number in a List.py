def nth_largest(nums, n):
    if n < 1:
        return None
    return sorted(nums, reverse=True)[n - 1]

nums = [14, 67, 48, 23, 5, 62]
n = int(input("Enter the value of N: "))
print(nth_largest(nums, n))
