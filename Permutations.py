def permute(nums):
    def backtrack(start, end):
        if start == end:
            result.append(nums[:])
        for i in range(start, end):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1, end)
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack(0, len(nums))
    return result

nums = [1, 1, 2]
print(permute(nums))  # Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
