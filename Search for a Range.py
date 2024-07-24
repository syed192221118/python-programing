def searchRange(nums, target):
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left

    first = findFirst(nums, target)
    last = findLast(nums, target)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    return [first, last]

nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))  # Output: [3, 4]
