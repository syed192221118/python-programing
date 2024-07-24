def insertElement(nums, element, index):
    nums.insert(index, element)
    return nums

nums = [47, 34, 21, 89, 12]
element = 100
index = 4
print(insertElement(nums, element, index))  # Output: [12, 21, 34, 100, 47, 89]
