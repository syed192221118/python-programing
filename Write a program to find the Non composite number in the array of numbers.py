def non_composite(nums):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False

    return [num for num in nums if not is_composite(num)]

nums = [26, 28, 47, 26, 43, 51, 29]
print(non_composite(nums))
