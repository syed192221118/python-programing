def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)
    result = []
    for num in nums:
        result.append(sorted_nums.index(num))
    return result

nums = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums))  # Output: [4, 0, 1, 1, 3]
ChildProcessError
