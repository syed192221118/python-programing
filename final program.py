def search_range(nums, target):
    def find_first(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def find_last(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right

    first = find_first(nums, target)
    last = find_last(nums, target)
    if first <= last:
        return [first, last]
    else:
        return [-1, -1]

nums = [5, 7, 7, 8, 8, 10]
target = 8
print(search_range(nums, target))  # Output: [3, 4]
