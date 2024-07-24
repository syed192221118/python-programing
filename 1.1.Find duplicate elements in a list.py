def find_duplicates(lst):
    duplicates = []
    for i in lst:
        if lst.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates

lst = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 9, 1]
print(find_duplicates(lst))  # Output: [1, 2, 3]
