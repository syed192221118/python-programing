def count_composite(nums):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False

    return sum(1 for num in nums if is_composite(num))

nums = [16, 18, 27, 16, 23, 21, 19]
print(count_composite(nums))
